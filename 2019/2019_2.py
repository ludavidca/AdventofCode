data = [int(x) for x in open("2.in","r").read().split(",")]

data[1] = 12
data[2] = 2

i = 0
while True:
    if data[i] == 1:
        firstnum = data[data[i+1]]
        sndnum = data[data[i+2]]
        result = firstnum + sndnum
        data[data[i+3]] = result
    elif data[i] == 2:
        firstnum = data[data[i+1]]
        sndnum = data[data[i+2]]
        result = firstnum * sndnum
        data[data[i+3]] = result
    elif data[i] == 99:
        break
    
    i+=4
   

print(data[0])