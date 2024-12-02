data = []
safe_count = 0

with open("input_data.txt") as f:
    for i in f:
        j = [int(x) for x in i.split()]
        data.append(j)

for i,j in enumerate(data):
    safe = True
    if j[0] > j[-1]:
        j.reverse()
    for k in range(len(j)-1):
        if j[k+1] - j[k] < 1 or j[k+1] - j[k] > 3:
            safe = False
    if safe:
        safe_count += 1

print(safe_count)