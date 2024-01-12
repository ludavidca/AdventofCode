data = [[int(y) for y in x] for x in open("2021_9.in", "r").read().split("\n")]

print(data)

def getleft(x,y):
    if data[y][x] < data[y][x-1]:
        return 1
    else:
        return 0

def getright(x,y):
    if data[y][x] < data[y][x+1]:
        return 1
    else:
        return 0
    
def getabove(x,y):
    if data[y][x] < data[y-1][x]:
        return 1
    else:
        return 0

def getbelow(x,y):
    if data[y][x] < data[y+1][x]:
        return 1
    else:
        return 0

lowareas = []

for y in range(len(data)): 
    for x in range(len(data[y])):
        print(f'{x} {y}')
        print(lowareas)
        if y == 0 and x == 0:
            i = 0
            i += getright(x,y)
            i += getbelow(x,y)
            if i == 2:
                lowareas.append(data[y][x])
        elif y == 0 and x == len(data[0])-1:
            i = 0
            i += getleft(x,y)
            i += getbelow(x,y)
            if i == 2:
                lowareas.append(data[y][x])
        elif y == len(data)-1 and x == 0:
            i = 0
            i += getright(x,y)
            i += getabove(x,y)
            if i == 2:
                lowareas.append(data[y][x])
        elif y == len(data)-1 and x == len(data[0])-1:
            i = 0
            i += getleft(x,y)
            i += getabove(x,y)
            if i == 2:
                lowareas.append(data[y][x])
        elif y == 0:
            i = 0
            i += getleft(x,y)
            i += getright(x,y)
            i += getbelow(x,y)
            if i == 3:
                lowareas.append(data[y][x])
        elif y == len(data)-1:
            i = 0
            i += getleft(x,y)
            i += getright(x,y)
            i += getabove(x,y)
            if i == 3:
                lowareas.append(data[y][x])
        elif x == 0:
            i = 0
            i += getbelow(x,y)
            i += getright(x,y)
            i += getabove(x,y)
            if i == 3:
                lowareas.append(data[y][x])
        elif x == len(data[0])-1:
            i = 0
            i += getbelow(x,y)
            i += getleft(x,y)
            i += getabove(x,y)
            if i == 3:
                lowareas.append(data[y][x])
        else: 
            i = 0
            i += getbelow(x,y)
            i += getleft(x,y)
            i += getright(x,y)
            i += getabove(x,y)
            if i == 4:
                lowareas.append(data[y][x])


print(sum(lowareas)+len(lowareas))