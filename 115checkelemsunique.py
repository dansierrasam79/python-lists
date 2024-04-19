init_list = [2, 4, 6, 8, 10, 12, 14]
final_list = []
for num in init_list:
	count = 0
	for num2 in init_list:
		if num == num2:
			count += 1
	if count > 1:
		final_list.append(num)
if len(final_list) == 0:
	print(True)
else:
	print(False)