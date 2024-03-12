import random
import os
import sqlite3

user_home_dir = os.path.expanduser("~")
db_file_path = os.path.join(user_home_dir, "test.db")

# Establish a connection to the SQLite database
connection = sqlite3.connect("/Users/danieldinh/School/Research/CelebratoryTechApp/mydatabase.db")

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
top_matches = {"001":[2,2,2,3,2,3,2,1,4,1,2,3,1,2,4,2,3,1,2,2,3,3,4,4],
"002":[3,2,4,1,2,3,4,3,2,1,2,3,4,3,4,2,1,2,3,2,1,1,1,1],
"003":[2,1,4,3,2,1,3,2,4,1,2,3,2,1,2,1,2,3,4,3,2,1,2,1],
"004":[2,1,2,4,3,3,2,1,2,3,4,1,2,3,1,2,1,2,4,3,2,3,4,1],
"005":[3,3,2,2,2,3,4,1,2,2,1,3,4,2,1,2,4,3,2,3,2,1,3,1],
"006":[4,4,3,3,2,1,4,3,2,3,1,1,3,4,2,1,1,2,3,2,1,2,3,2],
"007":[1,2,4,3,2,3,2,1,2,2,4,4,3,2,1,2,3,4,4,3,2,2,3,1],
"008":[1,2,2,1,3,4,3,2,1,2,3,4,3,2,2,1,2,1,1,4,3,2,1,1],
"009":[2,1,3,1,2,4,3,2,3,2,3,4,1,2,3,4,2,3,4,5,3,2,4,2],
"010":[1,2,3,1,4,3,2,1,2,3,4,2,1,2,3,4,1,1,2,2,3,3,4,1],
"011":[3,2,4,1,2,4,3,3,1,1,1,4,2,3,3,2,4,4,2,3,3,2,1,4],
"012":[4,2,1,2,3,3,4,2,3,1,2,1,2,3,4,3,2,1,2,3,4,1,2,4],
"013":[1,3,4,2,3,4,4,3,1,3,2,1,4,3,1,2,4,4,3,4,1,2,3,4],
"014":[4,2,3,4,1,2,3,3,2,2,2,1,2,3,4,4,4,2,1,1,1,2,3,4],
"015":[1,1,1,4,4,2,2,3,4,1,2,3,3,2,2,2,4,4,1,2,3,4,2,3],
"016":[2,3,4,2,1,2,3,2,1,2,3,4,3,2,1,2,3,4,3,2,1,1,3,4],
"017":[3,2,1,2,3,4,3,2,1,2,3,2,1,2,2,2,3,2,1,2,3,4,2,1],
"018":[1,2,3,2,1,2,1,2,3,4,2,3,2,3,4,3,2,1,3,3,2,1,2,3],
"019":[3,3,4,3,2,1,2,3,2,3,2,1,2,3,2,1,2,3,4,1,2,1,2,1],
"020":[2,1,2,3,4,4,3,3,2,1,2,3,4,3,2,1,2,3,4,4,3,2,1,1]}

# group the three closest nodes to each node in arrays
# for user_id in queries:
#     top_matches[user_id] = QUERY

# find the frequencies of all nodes (how often they appear in top 3 groupings)
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
# key = ID, value = hits in the top matches dictionary 
# EXAMPLE OF DATA: {"004": 4}

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

# find the top 4 MOST present nodes
sorted_dict = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))

# Convert the sorted dictionary to a list of tuples
sorted_list = list(sorted_dict.items())
# find the top 5 nodes
sorted_list = sorted_list[:5]

top_five = {}

# Extract the keys of the top 5 entries
for key,value in sorted_dict.items():
    if value in top_five:
        top_five[key] = value


# assign all top nodes to different groups

groups = []



# find unique nodes in each of their lists and assign them to their own groups

# group all the nodes by their connection to the central nodes 
top_connections = {}

for key in top_five.keys():
    top_connections[key] = []

stragglers = []

for key in top_matches:
    if key not in top_connections.values():
        stragglers.append(key)

# check if one of the central nodes is in the top 3 of any of the nodes 
for key,value_list in top_matches.items():
    for top_key in top_five.keys():
        if top_key in value_list:
            # add the key of the values list in which the central node appears 
            top_connections[top_key].append(key)

# assign to groups! 
groups_round3_best = [[],[],[],[],[]]

# FROM CHATGPT 

# Iterate through the dictionary
for key, values_list in top_connections.items():
    # Iterate through the values list
    for item in values_list:
        # Check if the item is unique
        # skip over duplicates
        if item not in sum(top_connections.values(), []):
            # Add the item to the list corresponding to its key in the nested list
            groups_round3_best[list(top_connections.keys()).index(key)].append(item)
            # remove the value
            values_list.remove(item)

# assign stragglers and duplicates 
i = 0
j = 0
for l in groups_round3_best:
    while len(l) < 4:
        # theres an issue with this --> improper indexing
        # # add the duplicate connections
        # l.append(top_connections[l][i]) # giving error
        # i += 1
        # if len(l) >= 4:
        #     break
        # add the nodes that did not match with any central node
        l.append(stragglers[j])
        j += 1

print("Group 3 (Best Matches): ", groups_round3_best)
        