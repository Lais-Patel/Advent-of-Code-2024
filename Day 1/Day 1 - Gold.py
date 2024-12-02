list_1 = []
list_2 = []
sim_dict = {}
sim_score = 0

with open("input_data.txt") as f:
    for i in f:
        x = i.split()
        sim_dict[int(x[0])] = 0
        list_1.append(int(x[0]))
        list_2.append(int(x[1]))

for i,j in enumerate(list_2):
    try:
        sim_dict[j] += 1
    except:
        continue

for i,j in enumerate(list_1):
    sim_score += j*sim_dict[j]

print(sim_score)