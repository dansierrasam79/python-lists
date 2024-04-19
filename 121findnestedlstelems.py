init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
init_list2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
final_list = []
for lst in init_list2:
	temp_list = []
	for num in lst:
		if num in init_list:
			temp_list.append(num)
	final_list.append(temp_list)
print(final_list)