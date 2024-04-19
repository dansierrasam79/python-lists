init_list1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
init_list2 = [1, 1, 2, 4, 5, 6]
for item in init_list2:
    if item in init_list1:
        init_list1.remove(item)
print(init_list1)