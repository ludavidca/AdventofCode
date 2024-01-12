data = [int(x) for x in open("2021_7.in", "r").read().split(",")]

maximum = max(data)
fuellist = []

for hpos in range(maximum):
    fuelcost = 0
    for individualpos in data:
        fuel = abs(individualpos-hpos)
        fuelcost += fuel
    fuellist.append(fuelcost)

minfuel = min(fuellist)

print(minfuel)