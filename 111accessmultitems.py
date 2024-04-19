init_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
index_list = [0, 3, 5, 7, 10]
final_list = []
for num in index_list:
	final_list.append(init_list[num])
print(final_list)