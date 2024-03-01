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

print("Groups:", groups)
