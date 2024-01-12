data = [str(x) for x in open("2021_3.in","r").read().split("\n")]



data1 = [x for x in data]


def more1or0(list, i): #returns 0 or 1 depending on the given list
    count1 = 0
    count0 = 0
    for j in range(len(list)):
        if list[j][i] == "0":
            count0 +=1
        if list[j][i] == "1":
            count1 +=1

    if count0 > count1:
        return 0
    elif count0 < count1: 
        return 1
    elif count0 == count1:
        return 1
    
def less1or0(list,i):
    count1 = 0
    count0 = 0
    for j in range(len(list)):
        if list[j][i] == "0":
            count0 +=1
        if list[j][i] == "1":
            count1 +=1

    if count0 > count1:
        return 1
    elif count0 < count1: 
        return 0
    elif count0 == count1:
        return 0

dellist = []

for i in range(len(data[0])): #scan for length of each binary num
    cnt = 0
    if len(data) > 1: #stop when there is only one left
        x = less1or0(data1,i)
        for j in range(len(data)): #scan through everything
            if data[j-cnt][i] != str(more1or0(data, i)): #
                dellist.append(more1or0(data, i))
                del data[j-cnt]
                cnt += 1

dellist1 = []
for i in range(len(data1[0])):
    cnt = 0
    if len(data1) > 1:
        x = less1or0(data1,i)
        dellist1.append(i)
        for j in range(len(data1)):
            if data1[j-cnt][i] != str(x):
                del data1[j-cnt]
                cnt += 1


x = int(str(data1[0]),2)
y = int(str(data[0]),2)

print(dellist1)
print(dellist)
print(x*y)




