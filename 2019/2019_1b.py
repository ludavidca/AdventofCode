i = open("1.in","r").read()
data = [int(x) for x in open("1.in","r").read().split("\n")]

def fuelfunction(mass):
    fuel = mass//3 -2
    if fuel < 0:
        return 0 
    fuel += fuelfunction(fuel) 
    return fuel

totalfuel = 0

for i in data:
    mass = i
    fuel = fuelfunction(mass)
    totalfuel = totalfuel + fuel


print(totalfuel)

