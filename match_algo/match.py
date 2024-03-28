import random
import os
import sqlite3

user_home_dir = os.path.expanduser("~")
db_file_path = os.path.join(user_home_dir, "test.db")

# Establish a connection to the SQLite database
connection = sqlite3.connect("Responses.sql")

# Create a cursor object
cursor = connection.cursor()
# # matching algorithm for iterations of participant kahoot testing
# participants = [i for i in range(1, 21)]

# # round 1: random
# # 20 participants, sectioned into 5 groups of 4
# generated = [0,0,0,0,0]
# groups_round1_random = [[],[],[],[],[]]

# # loop through all participants
# for j in range(20):
#     # generate a random number between 0 and 4
#     rand_num = random.randint(0, 4)

#     # check if the group corresponding to the random number has less than 4 elements
#     if len(groups_round1_random[rand_num]) < 4:
#         # if yes, append the current index to that group
#         groups_round1_random[rand_num].append(j)
#         generated[rand_num] += 1

#     # if the group has already been filled with 4 elements, pick a different random number
#     else:
#         while len(groups_round1_random[rand_num]) >= 4:
#             rand_num = random.randint(0, 4)
#         groups_round1_random[rand_num].append(j)
#         generated[rand_num] += 1

# print("Groups Round 1:", groups_round1_random)

# import the data from the database 

# Round 2
# based on MIXED communication styles (across the spectrum of different answers)

# Construct the SQL query to fetch user response
users = {}

for i in range(1, 21):
    user_id = '{:03d}'.format(i)
    user_response = '''
        SELECT * FROM Responses WHERE UserID = '{}'
        '''.format(user_id)
    cursor.execute(user_response)
    user_answer = cursor.fetchone()

    query = '''
    SELECT UserID,
        (CASE WHEN Question1 = '{0}' THEN 1 ELSE 0 END +
            CASE WHEN Question8 = '{1}' THEN 1 ELSE 0 END +
            CASE WHEN Question11 = '{2}' THEN 1 ELSE 0 END +
            CASE WHEN Question21 = '{3}' THEN 1 ELSE 0 END) AS match_score
    FROM Responses
    WHERE UserID != '{4}'
    ORDER BY match_score ASC
    LIMIT 3;
    '''.format(user_answer[1], user_answer[8], user_answer[11], user_answer[21], user_id )

    cursor.execute(query)
    user_match = cursor.fetchall()

# Round 3
# based on CLOSEST matches (participants who are the most similar in their answers)

# EXAMPLE OF DATA: {"001": ["002","004","007"], "002": ["003","006","019"] }
# top_matches = {}

# example of data

# group the three closest nodes to each node in arrays
# for user_id in queries:
#     top_matches[user_id] = QUERY

# find the frequencies of all nodes (how often they appear in top 3 groupings)
users = {}
top_matches = {}

for i in range(1, 21):
    user_id = '{:03d}'.format(i)

    user_response = '''
        SELECT * FROM Responses WHERE UserID = '{}'
        '''.format(user_id)
    cursor.execute(user_response)
    user_answer = cursor.fetchone()

    query = '''
        SELECT UserID,
            (CASE WHEN Question1 = '{0}' THEN 1 ELSE 0 END +
                CASE WHEN Question2 = '{1}' THEN 1 ELSE 0 END +
                CASE WHEN Question3 = '{2}' THEN 1 ELSE 0 END +
                CASE WHEN Question4 = '{3}' THEN 1 ELSE 0 END +
                CASE WHEN Question5 = '{4}' THEN 1 ELSE 0 END +
                CASE WHEN Question6 = '{5}' THEN 1 ELSE 0 END +
                CASE WHEN Question7 = '{6}' THEN 1 ELSE 0 END +
                CASE WHEN Question8 = '{7}' THEN 1 ELSE 0 END +
                CASE WHEN Question9 = '{8}' THEN 1 ELSE 0 END +
                CASE WHEN Question10 = '{9}' THEN 1 ELSE 0 END +
                CASE WHEN Question11 = '{10}' THEN 1 ELSE 0 END +
                CASE WHEN Question12 = '{11}' THEN 1 ELSE 0 END +
                CASE WHEN Question13 = '{12}' THEN 1 ELSE 0 END +
                CASE WHEN Question14 = '{13}' THEN 1 ELSE 0 END +
                CASE WHEN Question15 = '{14}' THEN 1 ELSE 0 END +
                CASE WHEN Question16 = '{15}' THEN 1 ELSE 0 END +
                CASE WHEN Question17 = '{16}' THEN 1 ELSE 0 END +
                CASE WHEN Question18 = '{17}' THEN 1 ELSE 0 END +
                CASE WHEN Question19 = '{18}' THEN 1 ELSE 0 END +
                CASE WHEN Question20 = '{19}' THEN 1 ELSE 0 END +
                CASE WHEN Question21 = '{20}' THEN 1 ELSE 0 END +
                CASE WHEN Question22 = '{21}' THEN 1 ELSE 0 END +
                CASE WHEN Question23 = '{22}' THEN 1 ELSE 0 END +
                CASE WHEN Question24 = '{23}' THEN 1 ELSE 0 END) AS match_score
        FROM Responses
        WHERE UserID != '{24}'
        ORDER BY match_score DESC
        LIMIT 3;
        '''.format(user_answer[1], user_answer[2], user_answer[3], user_answer[4], user_answer[5], user_answer[6], user_answer[7], user_answer[8], user_answer[9], user_answer[10], user_answer[11], user_answer[12], user_answer[13], user_answer[14], user_answer[15], user_answer[16], user_answer[17], user_answer[18], user_answer[19], user_answer[20], user_answer[21], user_answer[22], user_answer[23], user_answer[24], user_id )

    cursor.execute(query)
    user_match = cursor.fetchall()
    
    matched_user_ids = [match[0] for match in user_match]
    users[i] = matched_user_ids

# key = ID, value = hits in the top matches dictionary 
# EXAMPLE OF DATA: {"004": 4}
for user_id in users:
    top_matches[user_id] = users[user_id]

frequencies = {}
for value in top_matches.values():
    # loop through all indices in array 
    for element in value:
        # increment value if already in dictionary
        if element in frequencies.keys():
            frequencies[element] += 1
        # add value if not already found in ductionary 
        else:
            frequencies[element] = 1

# print("FREQ", frequencies)

# find the top 4 MOST present nodes
sorted_dict = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))

# Convert the sorted dictionary to a list of tuples
sorted_list = list(sorted_dict.keys())
# find the top 5 nodes
sorted_list = sorted_list[:5]

# print("SORTED", sorted_list)

top_five = {}

# Extract the keys of the top 5 entries
for key,value in sorted_dict.items():
    if key in sorted_list:
        top_five[key] = value

print("TOP 5",top_five)
# assign all top nodes to different groups

groups = []

# find unique nodes in each of their lists and assign them to their own groups

# group all the nodes by their connection to the central nodes 
top_connections = {}

for key in top_five.keys():
    top_connections[key] = []

# check if one of the central nodes is in the top 3 of any of the nodes 
for key,value_list in top_matches.items():
    for top_key in top_five.keys():
        if top_key in value_list:
            # add the key of the values list in which the central node appears 
            top_connections[top_key].append(key)

# assign to groups! 
groups_round3_best = [[],[],[],[],[]]

# FROM CHATGPT 

# stragglers = []

# find the nodes that are not in the top 5
# for key in top_matches.keys():
#     if key not in top_five.keys() and key not in top_five.values():
#         print("STRAGGLER", key)
#         stragglers.append(key)

# print top matches
print("TOP MATCHES", top_matches)

# Numbers from 1 to 20
numbers = range(1, 21)

# Check for missing numbers in values
print("VALUES OF TOP 5", top_five.values())
missing_values = [num for num in numbers if not any(num in sublist for sublist in top_connections.values())]
# check if any of the missing values is a central node (key in top_connections)
for num in missing_values:
    if num in top_connections.keys():
        missing_values.remove(num)


print("Missing numbers in values:", missing_values)

# Iterate through the dictionary
# keep track of current group in groups 
k = 0
for key, values_list in top_connections.items():
    groups_round3_best[k].append(key)
    # Iterate through the values list
    for item in values_list:
        # check if item is central node
        if item in top_connections.keys():
                # print("HEYYYYYY")
                top_connections[key].remove(item)

        # Check if the item is unique
        # skip over duplicates
        # check if element in values_list does not appear in any other key's values list
        if sum([item in v for k, v in top_connections.items() if k != key]) == 0 and item not in top_connections.keys():
            # put the item in the group with the corresponding key
            groups_round3_best[k].append(item)
            
            # remove singular item from top_connections dictionary 
            top_connections[key].remove(item)
            
            # # Find the group with the fewest members
            
            # min_group = min(groups_round3_best, key=len)
            # # Add the item to the group
            # min_group.append(item)

            

    k += 1




print("TOP CONNECTIONS AFTER REMOVAL", top_connections)
    
print("GROUPS ROUND 3 BEST ONLY UNIQUE", groups_round3_best)

# assign stragglers and duplicates 
i = 0
j = 0

# for l in groups_round3_best:
    # key = l[0]
    # # print("CURRENT KEY: ", key)
    # while len(l) < 4:
    #     # check if list out of range
    #     while i < 5:
    #         # print out the current group
    #         # print("CURRENT GROUP: ", l)
    #         # print top connections

    #         # print current key
    #         # print("CURRENT KEY: ", key)
    #     # theres an issue with this --> improper indexing
    #     # # add the duplicate connections
    #     # from top_connections, add next item corresponding to the group 
    #     # print("CURRENT KEY'S CONNECTIONS: ", top_connections[key])
    #     # print("CURRENT VAL TO ADD: ", top_connections[key][i])
    #     # check if current value is a central node
    #         if top_connections[key][i] in top_connections.keys():
    #             top_connections[key].remove(top_connections[key][i])
    #         # i -= 1
    #         # print out the value of i
    #             print("I: ", i)
    #             continue
    #         val_to_add = top_connections[key][i]
    #         l.append(val_to_add) 
    #         # remove the added value from the dictionary
    #         for key in top_connections.keys():
    #             if val_to_add in top_connections[key]:
    #                 top_connections[key].remove(val_to_add)

    #         i += 1
    #         print("CURRENT GROUP: ", l)
    #     if len(l) >= 4:
    #         break
    #     # add the nodes that did not match with any central node
    #     if j >= len(missing_values):
    #         # print current key
    #         # print("CURRENT KEY STRAGGLER: ", key)
    #         break
    #     l.append(missing_values[j])
    #     missing_values.remove(missing_values[j])
    #     j += 1
    #     print("TOP CONNECTIONS IN LOOP", top_connections)
    #     print("CURRENT KEY: ", key)
    
    # i = 0
    # j = 0

# print stragglers
print("STRAGGLERS: ", missing_values)

print("Group 3 (Best Matches): ", groups_round3_best)
        