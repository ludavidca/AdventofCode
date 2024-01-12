data = [str(x) for x in open("2021_4.in", "r").read().split("\n\n")]

winningnums = data[0].split(",")

scratchcardnums = data[1:]
data1 = [x.split("\n") for x in scratchcardnums]

#for i in scratchcardnums:  # loop through every card
#    data1.append(i.split("\n"))  # split into appropriate rows

data1 = [[x.split(" ") for x in y] for y in data1]

#for i in data1:  # loop through every card
#    for j in range(len(i)):  # loop through every row in every card using indices
#        i[j] = i[j].split(" ")

for i in data1:
    for j in i:
        cnt = 0
        for k in range(len(j)):
            if j[k-cnt] == "":
                del j[k-cnt]
                cnt += 1

#create columns in lists: data1[card][row:0-4, column:5-9]



for i in data1:
    for j in range(len(i)): #loop though the five rows
        addedlist = []
        for k in range(5):
            addedlist.append(i[k][j])
        i.append(addedlist)       

# find how many numbers are needed to be called in order for a win in each row/column

#[numcalled, cardnum, row/colnum]
winlist = [1000,1000,1000]

for i in range(len(data1)): # loop each scratchcard
    for j in range(len(data1[i])): #loop through rows and columns
        localwin = []
        for k in range(len(data1[i][j])): #loop through each string character of the list
            x = winningnums.index(data1[i][j][k])
            localwin.append(x)
            
            if len(localwin) == 5:
                rowwinnum = max(localwin)
            
                if rowwinnum < winlist[0]:
                    winlist[0] = rowwinnum
                    winlist[1] = i
                    winlist[2] = j

callednums = winningnums[:winlist[0]+1]

winningscratch = data1[winlist[1]][:5]

sumlist = []
for i in winningscratch:
    for k in i:
        if k not in callednums:
            sumlist.append(int(k))

lastcall = int(winningnums[winlist[0]])
sumUncalled = sum(sumlist)
print(lastcall*sumUncalled)