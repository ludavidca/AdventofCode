data = [[[z for z in y.split(" ")] for y in x.split(" | ")] for x in open("2021_8.in", "r").read().split("\n")]

targetlen = {2:1,3:7,4:4,7:8}
outputlist = []
for x in data:
    datalist = [[],[],[],[],[],[],[],[],[],[]] #stores digits start from 0
    targeteddata = x[0]
    cnt = 0
    for ii in range(len(targeteddata)):
        if len(targeteddata[ii-cnt]) == 2:
            for iii in targeteddata[ii-cnt]:
                datalist[1].append(iii)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt+=1
        elif len(targeteddata[ii-cnt]) == 3:
            for iii in targeteddata[ii-cnt]:
                datalist[7].append(iii)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt+=1
        elif len(targeteddata[ii-cnt]) == 4:
            for iii in targeteddata[ii-cnt]:
                datalist[4].append(iii)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt+=1
        elif len(targeteddata[ii-cnt]) == 7:
            for iii in targeteddata[ii-cnt]:
                datalist[8].append(iii)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt+=1

    cnt = 0
    for ii in range(len(targeteddata)): #check for 9
        templist = []
        for iii in targeteddata[ii-cnt]:
            templist.append(iii)

        if all(char in templist for char in datalist[4]):
            for i in templist:
                datalist[9].append(i)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt += 1
        elif len(templist) ==6 and all(char in templist for char in datalist[7]):
            for i in templist:
                datalist[0].append(i)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt += 1
        elif len(templist) ==5 and all(char in templist for char in datalist[7]):
            for i in templist:
                datalist[3].append(i)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt += 1
        elif len(templist) == 6:
            for i in templist:
                datalist[6].append(i)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt += 1
    
    cnt = 0
    for ii in range(len(targeteddata)): #check for 9
        templist = []
        for iii in targeteddata[ii-cnt]:
            templist.append(iii)
        if all(char in datalist[9] for char in templist):
            for i in templist:
                datalist[5].append(i)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt += 1
        else:
            for i in templist:
                datalist[2].append(i)
            targeteddata.remove(targeteddata[ii-cnt])
            cnt += 1
    
    orgoutput = x[1]
    newoutput = ""
    for untransnum in orgoutput:
        for ii in range(len(datalist)):
            listchar = []
            for iii in untransnum:
                listchar.append(iii)
            
            if all(char in listchar for char in datalist[ii]) and len(listchar) == len(datalist[ii]):
                newoutput += str(ii)
    outputlist.append(int(newoutput))
        
print(sum(outputlist))
