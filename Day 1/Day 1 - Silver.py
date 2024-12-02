list_1 = []
list_2 = []
total_dist = 0

with open("input_data.txt") as f:
    for i in f:
        x = i.split()
        list_1.append(int(x[0]))
        list_2.append(int(x[1]))


list_1.sort()
list_2.sort()
for i,j in enumerate(list_1):
    total_dist += abs(j-list_2[i])
print(total_dist)
