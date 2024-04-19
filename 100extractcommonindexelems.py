init_list = [1, 1, 3, 4, 5, 6, 7]
init_list2 = [0, 1, 2, 3, 4, 5, 7]
init_list3 = [0, 1, 2, 3, 4, 5, 7]
final_list = []
for i in range(0, len(init_list)):
	if init_list[i] == init_list2[i] and init_list[i] == init_list3[i]:
		final_list.append(init_list[i])
print(final_list)
