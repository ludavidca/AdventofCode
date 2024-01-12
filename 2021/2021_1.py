data = [int(x) for x in open("2021_1.in","r").read().split("\n")]

summeddata = []
for  i in range(len(data)-2):
    sum = data[i] + data[i+1] + data[i+2]
    summeddata.append(sum)
    

x = 0
for i in range(len(summeddata)-1):
    if summeddata[i] < summeddata[i+1]:
        x+=1

print(x)
