data = [str(x) for x in open("2023_4.in","r").read().split("\n")]

adjdata1 = []
for i in data:
    i = i.split(": ")
    i = i[1]
    adjdata1.append(i)

adjdata2 = []
for i in adjdata1:
    i = i.replace("  ", " ")
    i = i.split(" | ")
    i = [i[0].split(" "), i[1].split(" ")]
    adjdata2.append(i)

print(adjdata2)
numcontains = []
for i in adjdata2:
    x = 0 
    for j in range(len(i[0])):
        if i[0][j] in i[1]:
            x+=1
    numcontains.append(x)



finalpoints = []

for i in numcontains:
    points = 2 ** (int(i)-1)
    if i == 0:
        points = 0
    finalpoints.append(points)

print(sum(finalpoints))

