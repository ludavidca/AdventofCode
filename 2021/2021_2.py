data = [str(x) for x in open("2021_2.in","r").read().split("\n")]

x = 0 
depth = 0
aim = 0

for i in data:
    if i[0:7] == "forward":
        x += int(i[-1])
        depth += aim* int(i[-1])

    if i[0:2] == "up":
        aim -= int(i[-1])
    
    if i[0:4] == "down":
        aim += int(i[-1])
    
   

print(x*depth)