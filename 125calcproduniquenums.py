init_list = [10, 20, 30, 40, 20, 50, 60, 40]
final_list = []
for num in init_list:
	if num not in final_list:
		final_list.append(num)
prod = 1
for num in final_list:
	prod = prod*num
print(prod)