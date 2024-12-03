list_ = []
data = ""
total = 0
add = True

with open("input_data.txt") as f:
    data += (f.read()).replace("\n","")

def findfunction(add):
    count = data.find("mul(") + 4
    doex = data.rfind("do()", 0, count)
    dontex = data.rfind("don't()", 0, count)

    if doex > dontex:
        add = True
    if dontex > doex:
        add = False
    print(f"Do({doex}) > Don't({dontex})) = {add}")

    y = data[count]

    while y.isdigit():
        count += 1
        y += data[count] 
     
    if y.endswith(",") and add == True:
        y = y.split(",")
    else:
        return False
    
    count += 1
    y[1] += data[count]

    while y[1].isdigit():
        count += 1
        y[1] += data[count]
    
    if y[1].endswith(")") and add == True:
        y[1] = y[1].replace(")","")
        return y
    else:
        return False
    
while data.find("mul(") != -1:
    check = findfunction(add)
    if check != False and add == True:
        list_.append(check)
    try:
        data = data.replace("mul(",".",1)
    except:
        break

for i,j in enumerate(list_):
    total += int(j[1])*int(j[0])

print(total)
