aList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
elemList = []
listsorted = []
finalsortedlist = []

for item in aList:
    elemList.append(item[1])

listsorted = elemList.sort()

for i in range(0, len(aList)):
    for j in range(0, len(aList)):
        if elemList[i] == aList[j][1]:
            finalsortedlist.append(aList[j])

print(finalsortedlist)



                    


        
     