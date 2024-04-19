aList = [1, 1, 2, 3, 4, 4, 5, 1]
bList = []
cList = []
n = 3
count = 0
temp_list = []
for i in range(0,len(aList)):
    if i < n:
        bList.append(aList[i])
    else:
        cList.append(aList[i])

print(bList, cList)
