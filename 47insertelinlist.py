aList = [0,1,2,3,4,5,6,7,8,9,10]
final_list = []
insert_list = [10,9,8,7,6,5,4,3,2,1,0]
for i in range(0, len(aList)):
    final_list.append(aList[i])
    final_list.append(insert_list[i])
print(final_list)