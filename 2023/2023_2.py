data = [str(x) for x in open("2023_2.in","r").read().split("\n")]

reqlist = [12,13,14]

data1 = []
for i in data:
    i = i.split(": ")
    i = i[1]
    data1.append(i)

adjlist1 = []

for i in data1:
    adjstr = ""
    for x in range(len(i)):
        if i[x].isnumeric() or i[x].__contains__(",") or i[x].__contains__(";") or i[x].__contains__("r") or i[x].__contains__("b") or i[x].__contains__("g"):
            adjstr += i[x]
    adjlist1.append(adjstr)

#breakdown into cases


adjlist2 = []
for i in adjlist1:
    el = i.split(";")
    adjlist2.append(el)

print(adjlist1)
print(adjlist2)

#create a list of most number of each color in each case situation
minlist = []

for i in adjlist2:
    minnum = [0,0,0] #r,gr,b
    for x in i:
        x = x.split(",")
        for y in x:
            if y[-2:] == "gr":
                numgr = int(y[:-2])
                if minnum[1]<numgr:
                    minnum[1] = numgr
            elif y[-1] == "r":
                numr = int(y[:-1])
                if minnum[0]<numr:
                    minnum[0] = numr
            elif y[-1] == "b":
                numb = int(y[:-1])
                if minnum[2]<numb:
                    minnum[2] = numb
    minlist.append(minnum)
        
print(minlist)

suitablegames = []

for i in range(len(minlist)):
    p = 0
    for x in range(3):
        if minlist[i][x] <= reqlist[x]:
            p += 1
    if p == 3:
        suitablegames.append(i+1)

print(sum(suitablegames))
