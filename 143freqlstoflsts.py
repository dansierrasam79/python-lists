init_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
final_list = []
final_dict = {}
for i in range(0, len(init_list)):
    for j in range(0, len(init_list[i])):
        final_list.append(init_list[i][j])

for item in final_list:
    count = 0
    for item2 in final_list:
        if item == item2:
            count += 1
    final_dict[item] = count
print(final_dict)