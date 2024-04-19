init_list = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
final_list = []
last_num = 999
for num in init_list:
	if num == last_num:
		if num not in final_list:
			final_list.append(num)
	else:
		last_num = num
print(final_list)
