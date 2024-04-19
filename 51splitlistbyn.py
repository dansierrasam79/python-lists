aList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
final_list = []
n = 3
count = 0
for i in range(0, 3):
    tempList = []
    for j in range(i,len(aList),n):
        tempList.append(aList[j])
    final_list.append(tempList)
print(final_list)