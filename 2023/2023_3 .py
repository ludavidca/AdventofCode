data = [str(x) for x in open("2023_3.in", "r").read().split("\n")]

sumschematic = []
unspecialcharacters = "0,1,2,3,4,5,6,7,8,9,.".split(",")
numbers = "0,1,2,3,4,5,6,7,8,9".split(",")

for i in range(len(data)):
    data[i] = data[i] + "."

print(data)


for i in range(len(data)):
    num = ""
    listindex = []
    for j in range(len(data[i])): #loop through each index in schematic, then find the num
        
        if data[i][j].isnumeric(): #if it is numeric, add to the number and append the index
            num += data[i][j]
            listindex.append(j) 
        
        #add the dot
    
        elif data[i][j] not in numbers: # if it is a period or a special thing, go for checking
            if num != "":   # if there is a valid number, then
                
                # check if first list index is zero or if the last listindex is equal to the data of i, and if it is do not add or decrease the number
                
                if listindex[0] == 0:
                    firstindex = 0
                else:
                    firstindex = listindex[0] -1 
                    
                if listindex[-1] == len(data[i]):
                    lastindex = len(data[i])
                else:
                    lastindex = listindex[-1] +1

                x = 0

                #checking if the characters that are left and right are special
                if data[i][firstindex] not in unspecialcharacters:
                    x+=1

                if data[i][lastindex] not in unspecialcharacters:

                    x+=1

                
                for k in range(firstindex, lastindex+1): #loop through each character in the data above and below to find if they match
                    if i-1>=0: #check if there is a row above
                        if data[i-1][k] not in unspecialcharacters:
                            x += 1
                   
                    
                    
                    if i+1 <= len(data)-1: #check if there is a row below
                        if data[i+1][k] not in unspecialcharacters:
                            x += 1

                
                if x>0:
                    sumschematic.append(num)
                    num = ""
                    listindex = []
                
                else:
                    num = ""
                    listindex = []
                    
print(sumschematic)

total = 0
for i in sumschematic:
    total += int(i)
            
print(total)

# need to account for last numbers, not scanning last numbers, must change



        
    
        



