list1 = []
list2 = []

with open('inputs', 'r') as file:
    # Read each line in the file
    for line in file:
        values = line.split("   ")
        list1.append(values[0])
        list2.append(values[1])

list1.sort()
list2.sort()

# For question 2
dico1 = {}
dico2 = {}

total_distance = 0
for i in range(len(list2)):
    val1 = int(list1[i])
    val2 = int(list2[i])
    total_distance += abs(val1 - val2)

    # for question 2
    if val1 in dico1:
        dico1[val1] += 1
    else:
        dico1[val1] = 1

    if val2 in dico2:
        dico2[val2] += 1
    else:
        dico2[val2] = 1



# solution n°1
print("total_distance =",total_distance)

similarity_score_sum = 0

for elem in dico1:
    if elem in dico2:
        # sum = number * (number of time it's present in list1) * (number of time it's present in list2)
        similarity_score_sum += elem * dico1[elem] * dico2[elem]

print("similarity_score_sum =",similarity_score_sum) 




