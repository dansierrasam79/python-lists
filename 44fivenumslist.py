aList = []
tempList = []
count = 0
for i in range(0,20):
    count += 1
    if count != 5:
        tempList.append(i)
    else:
        tempList.append(i)
        aList.append(tempList)
        tempList = []
        count = 0
print(aList)
