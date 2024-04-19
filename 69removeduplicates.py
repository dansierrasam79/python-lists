aList = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
final_list = []
for lst in aList:
    count = 0
    for lst2 in aList:
        count += 1
    if count >= 2:
        if lst not in final_list:
            final_list.append(lst)
print(final_list)