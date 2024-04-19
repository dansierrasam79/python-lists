aList = [1,2,2,3,4,5,6,6,6,7,8,9,9,10,10,10,10]
fList = []
count = 0
for item in aList:
    for item2 in aList:
        if item == item2:
            count += 1
    if count == 1:
        fList.append(item)
    count = 0

print(fList)