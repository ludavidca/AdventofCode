i = open("1.in","r").read()
data = [int(x) for x in open("1.in","r").read().split("\n")]

totalfuel = 0

for i in data:
    mass = i
    fuel = mass//3 -2
    totalfuel = totalfuel + fuel
    

print(totalfuel)

