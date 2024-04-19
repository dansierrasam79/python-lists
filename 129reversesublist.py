init_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
final_list = []
temp_list = []
for lst in init_list:
	temp_list = []
	for i in range(len(lst)-1,-1,-1):
		temp_list.append(lst[i])
	final_list.append(temp_list)
print(final_list)
