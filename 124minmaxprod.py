init_list = [(2, 7), (2, 6), (1, 8), (4, 9)]
temp_list = []
final_list = []
final_tup = ()
for tup in init_list:
	temp_list.append(tup[0]*tup[1])
final_list.append(min(temp_list))
final_list.append(max(temp_list))
final_tup = tuple(final_list)
print(final_tup)