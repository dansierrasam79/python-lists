init_list = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
init_list2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
final_list = []
for i in range(0,len(init_list)):
    temp_list = []
    temp_list.extend(init_list[i])
    temp_list.extend(init_list2[i])
    final_list.append(temp_list)
print(final_list)
