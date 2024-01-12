y = 0
list = []
for i in range(359281,820402):
    for x in range(0,5):
        if str(i)[x] == str(i)[x+1]:
            num1 = 0 
            for x in range(0,5):
                if int(str(i)[x]) <= int(str(i)[x+1]):
                    num1 += 1
                    if num1 == 5:
                        list.append(i)

uniquelist = []
for x in list:
    if x not in uniquelist:
        uniquelist.append(x)

print(uniquelist)
print(len(uniquelist))