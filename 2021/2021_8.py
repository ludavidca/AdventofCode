data = [[[z for z in y.split(" ")] for y in x.split(" | ")] for x in open("2021_8.in", "r").read().split("\n")]

print(data)
targetlen = {2:1,3:7,4:4,7:8}

x = 0
for i in range(len(data)):
    for ii in data[i][1]:
        if len(ii) in targetlen.keys:
            x += 1

print(x)