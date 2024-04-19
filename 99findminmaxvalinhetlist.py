init_list = ['Python', 3, 2, 4, 5, 'version']
int_type = type(1)
final_list = []
for item in init_list:
	if type(item) == int_type:
		final_list.append(item)
print(final_list)
print("minimum", min(final_list))
print("maximum", max(final_list))