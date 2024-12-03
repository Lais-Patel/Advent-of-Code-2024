list_ = []
data = ""
total = 0
add = True

with open("input_data.txt") as f:
    data += (f.read()).replace("\n","")

def findfunction():
    count = data.find("mul(") + 4
    y = data[count]

    while y.isdigit():
        count += 1
        y += data[count] 
     
    if y.endswith(","):
        y = y.split(",")
    else:
        return False
    
    count += 1
    y[1] += data[count]

    while y[1].isdigit():
        count += 1
        y[1] += data[count]
    
    if y[1].endswith(")"):
        y[1] = y[1].replace(")","")
        return y
    else:
        return False
    
while data.find("mul(") != -1:
    check = findfunction()
    if check != False:
        list_.append(check)
    try:
        data = data.replace("mul(",".",1)
    except:
        break

for i,j in enumerate(list_):
    total += int(j[1])*int(j[0])

print(total)
