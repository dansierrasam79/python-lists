aList = [0,1,2,3,4,5]

for i in range(0,len(aList),2):
    temp, temp2 = 0,0
    temp = aList[i]
    temp2 = aList[i+1]
    aList[i] = temp2
    aList[i+1] = temp
print(aList)
