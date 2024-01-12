
data = [str(x) for x in open("2023_1.in","r").read().split("\n")]

replaceList = []

for i in data:
    i = i.replace("one", "one1one")
    i = i.replace("two", "two2two")
    i = i.replace("three", "three3three")
    i = i.replace("four", "four4four")
    i = i.replace("five", "five5five")
    i = i.replace("six", "six6six")
    i = i.replace("seven", "seven7seven")
    i = i.replace("eight", "eight8eight")
    i = i.replace("nine", "nine9nine")
    replaceList.append(i)



listnum = []


for i in replaceList:
    num = ""
    for x in range(len(i)):
        if i[x].isnumeric() == True:
            num += str(i[x])
    listnum.append(num)

adjnum = []




for i in listnum:
    if len(i) == 0:
        pass
    elif len(i) == 1:
        adjnum.append(int(i+i))
    else:
        firststr = i[0]
        laststr = i[-1]
        finalnum = int(firststr + laststr)
        adjnum.append(finalnum)

print(replaceList)
print(adjnum)


print(sum(adjnum))