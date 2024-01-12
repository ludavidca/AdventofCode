data = [str(x) for x in open("2021_6.in","r").read().split(",")]

binnedlist = []
for i in range(9):
    binnedlist.append(0)

for i in data:
    binnedlist[int(i)] += 1

print(binnedlist)

for i in range(256):
    num0 = binnedlist.pop(0)
    binnedlist.append(num0)
    binnedlist[6] += num0
    print(binnedlist)

print(sum(binnedlist))