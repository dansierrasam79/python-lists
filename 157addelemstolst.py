init_list = [2, 4, 7, 0, 5, 8]
init_list2 = [2, 5, 8]
init_list3 = [0, 1]
init_list4 = [3, 3, -1, 7]
diff_list = []
final_list = []

for i in range(0,len(init_list)):
    final_list.append(init_list[i])
    if i < len(init_list2):
        final_list.append(init_list2[i])
    if i < len(init_list3):
        final_list.append(init_list3[i])
    if i < len(init_list4):
        final_list.append(init_list4[i])
print(final_list)