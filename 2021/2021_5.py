data = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in open('2021_5.in','r').read().split("\n")]

maxnum = [0,0] #x,y
for i in data:
    for j in i:
        if j[0]>maxnum[0]:
            maxnum[0] = j[0]
        if j[1]>maxnum[1]:
             maxnum[1] = j[1]

map = []
for i in range(maxnum[1]+1):
    templist = []
    for i in range(maxnum[0]+1):
        templist.append("0")
    map.append(templist)


def horizontalmove(y, startx, endx):
    total = startx + endx
    if startx > endx:
        startx = total -startx
        endx = total - endx

    for i in range(int(startx), int(endx)+1):
        map[y][i] = str(int(map[y][i])+1)

def verticalmove(x, starty, endy):
    total = starty + endy
    if starty > endy:
        starty = total -starty
        endy = total - endy
    
    for i in range(int(starty), int(endy)+1):
        map[i][x] = str(int(map[i][x])+1)
    

for i in data: #loop thorugh each set of 2 coordinate
    if i[0][1] == i[1][1]: # same y values
        horizontalmove(i[0][1], i[0][0],i[1][0])
    elif i[0][0] == i[1][0]: # same x values
        verticalmove(i[0][0], i[0][1],i[1][1])


score = 0
for i in map:
    for j in i:
        if int(j) >= 2:
            score+=1

print(score)