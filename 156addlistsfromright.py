init_list = [2, 4, 7, 0, 5, 8]
init_list2 = [3, 3, -1, 7]
final_list = []
init_list2.insert(0,0)
init_list2.insert(0,0)
for i in range(0,len(init_list)):
    final_list.append(init_list[i] + init_list2[i])
print(final_list)