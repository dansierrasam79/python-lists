init_list = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
max_occurences = 0
max_val = 999
for num in init_list:
	count = 0
	for num2 in init_list:
		if num == num2:
			count += 1
	if count > max_occurences:
		max_occurences = count
		max_val = num
print(max_val,max_occurences)