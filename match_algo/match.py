import random

# matching algorithm for iterations of participant kahoot testing
participants = [i for i in range(1, 21)]

# round 1: random
# 20 participants, sectioned into 5 groups of 4
generated = [0,0,0,0,0]
groups = [[],[],[],[],[]]

# loop through all participants
for j in range(20):
    # generate a random number between 0 and 4
    rand_num = random.randint(0, 4)

    # check if the group corresponding to the random number has less than 4 elements
    if len(groups[rand_num]) < 4:
        # if yes, append the current index to that group
        groups[rand_num].append(j)
        generated[rand_num] += 1

    # if the group has already been filled with 4 elements, pick a different random number
    else:
        while len(groups[rand_num]) >= 4:
            rand_num = random.randint(0, 4)
        groups[rand_num].append(j)
        generated[rand_num] += 1

print("Groups Round 1:", groups)

# import the data from the database 

# Round 2
# based on MIXED communication styles (across the spectrum of different answers)







# Round 3
# based on CLOSEST matches (participants who are the most similar in their answers)

# EXAMPLE OF DATA: {"001": ["002","004","007"], "002": ["003","006","019"] }
top_matches = {}

# group the three closest nodes to each node in arrays
for user_id in queries:
    top_matches[user_id] = QUERY RESPONSE 

# find the frequencies of all nodes (how often they appear in top 3 groupings)

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

top_four = dict(sorted_dict[:4])

# assign all top nodes to different groups

groups = []



# find unique nodes in each of their lists and assign them to their own groups

# group all the nodes by their connection to the central nodes 
top_connections = {}



for value in top_matches.keys():
    for key in top_four.keys():
        if 

# skip over duplicates

# assign stragglers and duplicates 
