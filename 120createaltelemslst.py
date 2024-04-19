init_list = ['red', 'black', 'white', 'green', 'orange']
final_list = []
for i in range(0, len(init_list)):
	if i % 2 == 0:
		final_list.append(init_list[i])
print(final_list)