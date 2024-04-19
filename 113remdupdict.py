init_list = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
for item in init_list:
	count = 0
	index_val = []
	for item2 in init_list:
		if item == item2:
			index_val.append(count)
		count += 1
	print(item,index_val)
	if len(index_val) > 1:
		init_list.pop(index_val[-1])
print(init_list)
