aList = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
final_list = []
count = 0
for pos in range(0,len(aList)-1):
    if aList[pos] == aList[pos+1] and aList[pos] != aList[pos-1]:
        final_list.append(aList[pos])
    elif aList[pos] != aList[pos+1] and aList[pos] != aList[pos-1]:
        final_list.append(aList[pos])
print(final_list)