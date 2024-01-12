import math

time = [63789468]
record = [411127420471035]


waystobeat = []
for i in range(len(time)):
    possibledistances = []

    for j in range(time[i]):
        totaltime = time[i]
        holdtime = j
        totaldistance = (totaltime-holdtime)*holdtime
        possibledistances.append(totaldistance)
    
    correcteddistances = []
    for k in possibledistances:
        if k > record[i]:
            correcteddistances.append(k)
    
    waystobeat.append(len(correcteddistances))

print(math.prod(waystobeat))

