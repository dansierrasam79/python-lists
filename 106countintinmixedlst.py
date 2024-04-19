init_list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
count = 0
for num in init_list:
	if type(num) == type(count):
		count += 1
print(count)
