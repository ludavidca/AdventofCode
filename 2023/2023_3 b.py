data = [str(x) for x in open("2023_3.in", "r").read().split("\n")]

sumschematic = []
unspecialcharacters = "0,1,2,3,4,5,6,7,8,9,.".split(",")
numbers = "0,1,2,3,4,5,6,7,8,9".split(",")

for i in range(len(data)):
    data[i] = data[i] + "."

specialcharacters = []

for i in data:
    for j in i:
        if j not in specialcharacters and j not in 