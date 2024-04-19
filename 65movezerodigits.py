aList = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
zero_list = []
final_list = []
for item in aList:
    if item != 0:
        final_list.append(item)
    else:
        zero_list.append(item)
final_list.extend(zero_list)
print(final_list)
