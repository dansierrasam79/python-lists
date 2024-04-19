aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
final_list = []
for num in aList:
    for num2 in aList:
        if num != num2:
            final_list.append([num,num2])
print(final_list)
