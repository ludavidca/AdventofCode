

data = [str(x) for x in open("3.in","r").read().split("\n")]
wire1 = data[0].split(",")
#wire1 = ["R10","D10","L9","D6", "R4"]
wire2 = data[1].split(",")
#wire2 = ["R2","D10","L9","D6", "R4"]

dirDict = ["L", "R", "U", "D"]


def createcoords(inputlist):
    x1 = 0
    y1 = 0
    dots1 = []

    for i in range(len(inputlist)):
        if inputlist[i][0] == "L":
            maxLineNum = int(inputlist[i][1:])
            for x in range(maxLineNum):
                x1 -= 1
                dots1.append((x1,y1))
                
        if inputlist[i][0] == "R":
            maxLineNum = int(inputlist[i][1:])
            for x in range(maxLineNum):
                x1 += 1
                dots1.append((x1,y1))
        if inputlist[i][0] == "U":
            maxLineNum = int(inputlist[i][1:])
            for x in range(maxLineNum):
                y1 += 1
                dots1.append((x1,y1))
        if inputlist[i][0] == "D":
            maxLineNum = int(inputlist[i][1:])
            for x in range(maxLineNum):
                y1 -= 1
                dots1.append((x1,y1))
    return dots1 

dots1 = createcoords(wire1)
dots2 = createcoords(wire2)

duplicates = list(set(dots1).intersection(dots2))

resultingsteps = []

for x in range(len(duplicates)):
    for i in range(len(dots1)):
        if dots1[i] == duplicates[x]:
            a = i+1
    for i in range(len(dots2)):
        if dots2[i] == duplicates[x]:
            b = i+1
    resultingsteps.append(a+b)


#result = min(ListofSteps)


print(min(resultingsteps))
        
