data = [int(x) for x in open("2021_7.in", "r").read().split(",")]

maximum = max(data)
fuellist = []

for hpos in range(maximum):
    fuelcost = 0
    for individualpos in data:
        i = abs(individualpos-hpos)
        fuelcost += i*(i+1)/2 #factorial sum to improve performance
    fuellist.append(fuelcost) 

minfuel = min(fuellist)

print(minfuel)