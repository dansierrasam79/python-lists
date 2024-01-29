aList = [1,2,2,3,4,5,6,6,6,7,8,9,9,10,10,10,10]
aDict = {}
for item in aList:
    count = 0
    for item2 in aList:
        if item == item2:
            count += 1
    aDict[item] = count
print(aDict)
