init_list = [4, 5, 8, 9, 6, 10]
final_list = []
for i in range(1, len(init_list)):
	final_list.append(init_list[i]-init_list[i-1])
print(final_list)