data = [[str(x) for x in y.split("\n")] for y in open("2023_13.in", "r").read().split("/n/n")]


# find vertical mirrors
for i in range(len(data)): #loop through each image
    blanklist = []
    for x in range(len(data[i])):
        blanklist.append(0)

    for j in range(len(data[i])):
        for k in range(len(data[i][0])): # loop through characters of each line
            if data[i][k] == data[i][k+1]:
                blanklist[k] += 1
    
    print(blanklist)
    matchcolumn = blanklist.index(max(blanklist))
    coltoleft = matchcolumn + len(data[i])/2-0.5
    print(coltoleft)



