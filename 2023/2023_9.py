data = [str(x) for x in open("2023_09.in","r").read().split("\n")]
splittedData = [x.split(" ") for x in data]
intData = [[int(x) for x in y] for y in splittedData]

sumlist = []

for i in intData:
    dict = {}
    dict["numlist0"] = i
    for y in range(len(i) -1):
        name = "numlist" + str(y+1)
        dict[name] = []
    
    #now that info is in dictionary, loop through each item in the dictionaries
    
    for k in range(len(dict['numlist0'])-1):
        name = 'numlist'+ str(k)
        templist = []
        for j in range(len(dict[name])-1): #loopthrough individual nums        
            templist.append(dict[name][j+1]-dict[name][j])
            
        name2 = 'numlist' + str(k+1)
        dict[name2] = templist

    print(dict)
    sumEndNum = 0
    for a in reversed(range(len(dict))):
        name = 'numlist' + str(a)
        sumEndNum = dict[name][0] - sumEndNum
    sumlist.append(sumEndNum)

print(sum(sumlist))