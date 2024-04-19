init_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
init_list2 = [2, 2, 3, 1, 2, 6, 7, 9]
init_list3 = [2, 1, 3, 1, 2, 6, 7, 9]
count = 0
for i in range(0,len(init_list1)):
	if init_list1[i] == init_list2[i] and init_list1[i] == init_list3[i]:
		count += 1
print("Number of same pairs: ", count)