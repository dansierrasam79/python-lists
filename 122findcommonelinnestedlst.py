init_list = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
final_list = []
count = 0
for lst in init_list:
	for num in lst:
		count = 0
		for lst2 in init_list:
			if num in lst2:
				count += 1
				if count == 3:
					final_list.append(num)
	break;
print(final_list)
