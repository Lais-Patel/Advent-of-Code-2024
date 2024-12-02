data = []
unsafe = {}
safe_count = 0

with open("input_data.txt") as f:
    for i in f:
        j = [int(x) for x in i.split()]
        data.append(j)

undata = data[:]

for i,j in enumerate(data):
    safe = True
    if j[0] > j[-1]:
        j.reverse()
    if j[1] > j[-2]:
        print(f"{j[1]} > {j[-2]} = {j[1] > j[-2]}")
        j.reverse()
    for k in range(len(j)-1):
        if j[k+1] - j[k] < 1 or j[k+1] - j[k] > 3:
            safe = False
    if safe:
        safe_count += 1
        undata.remove(j)

for a,b in enumerate(undata):
    if j[0] > j[-1]:
        j.reverse()
    if j[1] > j[-2]:
        j.reverse()
    unsafe[str(b)] = False
    d = b[:]
    for c in range(len(b)):
        d.pop(c)
        #print(d,c)
        if d[0] > d[-1]:
            d.reverse()
        passes = 0
        for z in range(len(d)-1):
            if 0 < d[z+1] - d[z] < 4:
                passes += 1
                if passes == (len(d)-1):
                    unsafe[str(b)] = True
        
        d = b[:]
newsafe_count = 0
for q in unsafe:
    if unsafe[q]:
        newsafe_count += 1
        #print(q,unsafe[q])
for g in undata:
    pass#print(g)
print(newsafe_count)
print(safe_count)
print(safe_count+newsafe_count)