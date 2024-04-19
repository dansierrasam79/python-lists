init_list = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
sum_dict = {}
for lst in init_list:
	sum_dict[sum(lst)] = lst
sorted_sum_list = sorted(sum_dict.values())
print(sorted_sum_list)