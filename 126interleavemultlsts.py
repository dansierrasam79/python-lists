init_list1 = [1, 2, 3, 4, 5, 6, 7]
init_list2 = [10, 20, 30, 40, 50, 60, 70]
init_list3 = [100, 200, 300, 400, 500, 600, 700]
final_list = []
for i in range(0, len(init_list1)):
	final_list.append(init_list1[i])
	final_list.append(init_list2[i])
	final_list.append(init_list3[i])
print(final_list)