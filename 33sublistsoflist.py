aList = ['Tom', 'Dick', 'Harry', 'Mary', 'Jane', 'Anne']
fList = []
for i in range(0, len(aList)):
    tempList = []
    for j in range(0, i):
        tempList.append(aList[j])
    fList.append(tempList)
print(fList)