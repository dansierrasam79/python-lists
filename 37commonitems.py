aList = [0,1,2,3,4,5]
bList = [3,5,4,7,6]
fList = []

for item in aList:
    for item2 in bList:
        if item == item2:
            fList.append(item)

print(fList)
