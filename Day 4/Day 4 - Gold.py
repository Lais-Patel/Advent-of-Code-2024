xmas = []
word = ['X','M','A','S']
total = 0

with open("input_data.txt") as f:
    for i in f:
        i = i.replace("\n","")
        x = []
        for j in i:
            x.append(j)
        xmas.append(x)

def find_xmas(x,y):
    count = 0
    if xmas[x][y] == word[2]:
        for d in range(4):
            match(d):
                case 0:
                    try:
                        if xmas[x-1][y-1] == word[1] and xmas[x+1][y+1] == word[3] and xmas[x+1][y-1] == word[1] and xmas[x-1][y+1] == word[3] and (x-1) >= 0 and (y-1) >= 0:
                            count += 1
                    except:
                        continue
                case 1:
                    try:
                        if xmas[x-1][y-1] == word[1] and xmas[x+1][y+1] == word[3] and xmas[x+1][y-1] == word[3] and xmas[x-1][y+1] == word[1] and (x-1) >= 0 and (y-1) >= 0:
                            count += 1
                    except:
                        continue
                case 2:
                    try:
                        if xmas[x-1][y-1] == word[3] and xmas[x+1][y+1] == word[1] and xmas[x+1][y-1] == word[1] and xmas[x-1][y+1] == word[3] and (x-1) >= 0 and (y-1) >= 0:
                            count += 1
                    except:
                        continue
                case 3:
                    try:
                        if xmas[x-1][y-1] == word[3] and xmas[x+1][y+1] == word[1] and xmas[x+1][y-1] == word[3] and xmas[x-1][y+1] == word[1] and (x-1) >= 0 and (y-1) >= 0:
                            count += 1
                    except:
                        continue
                case _:
                    continue
    return count

for i in range(len(xmas)):
    for j in range(len(xmas)):
        total += find_xmas(i,j)
print("Total:",total)