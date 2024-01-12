for noun in range(100):
    for verb in range(100):
        data = [int(x) for x in open("2.in","r").read().split(",")]
        data[1] = noun
        data[2] = verb

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
        
        if data[0] == 19690720:
            num = 100* noun + verb
            print(num)
    