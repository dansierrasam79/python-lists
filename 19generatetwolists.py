aList = [1,2,3,4,5]
bList = [3,4,6,7,9]
fList = []

for item in aList:
    if item not in bList:
        fList.append(item)

for item in bList:
    if item not in aList:
        fList.append(item)

print(fList)
