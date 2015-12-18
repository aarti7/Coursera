AA = [3, 12, 9,3] # change to 2 same numbers, already sorted numbers
print AA
runover=0
k = 0
totalcomparison=0
for p in range(len(AA)):
    mee = 0
    for h in range(len(AA)-1 -runover): # adding 10 to len doesnt change anything.. how?  
        totalcomparison +=1
        if mee < len(AA)-1:
            if AA[mee+1] < AA[mee]:
                k = AA[mee]
                AA[mee] = AA[mee+1]
                AA[mee+1] = k
                mee +=1
            else:
                mee +=1
        else:
            pass

    runover +=1        

            
print "final array"
print AA, runover, totalcomparison