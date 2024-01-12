y = 0
possibilities = []
for i in range(359281,820402):
    for x in range(0,5):
        if str(i)[x] == str(i)[x+1]:
            num1 = 0 
            for x in range(0,5):
                if int(str(i)[x]) <= int(str(i)[x+1]):
                    num1 += 1
                    if num1 == 5:
                        possibilities.append(str(i))

possibilities = list(set(possibilities))

newpossibilities = []

for i in possibilities:
    if i[0] == i[1] !=i[2] or i[0] != i[1] == i[2] != i[3] or i[1] != i[2] == i[3] != i[4] or i[2] != i[3] == i[4] != i[5] or i[3] != i[4] == i[5]:
        newpossibilities.append(i)

print(len(newpossibilities))