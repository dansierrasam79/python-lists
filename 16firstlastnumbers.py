initList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
finalList = []

for i in range(0,5):
    finalList.append(initList[i]**2)

for j in range(24,30):
    finalList.append(initList[j]**2)

print(finalList)
