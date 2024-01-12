
data = [str(x) for x in open("2021_3.in","r").read().split("\n")]


gamma = ""
eplison = ""

count1 = 0
count0 = 0

for i in range(len(data[0])):
    for j in range(len(data)):
        if data[j][i] == "0":
            count0 +=1
        if data[j][i] == "1":
            count1+=1
    print(count1)
    if count0 > count1:
        gamma+= "0"
        eplison += "1"
        count1 = 0
        count0 = 0
    elif count0 < count1: 
        gamma+= "1"
        eplison += "0"
        count1 = 0
        count0 = 0


gammaint = int(gamma, 2)
eplisonint = int(eplison, 2)

print(gammaint*eplisonint)