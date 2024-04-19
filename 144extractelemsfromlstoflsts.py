first_elem_lst = []
third_elem_lst = []
init_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
for i in range(0, len(init_list)):
    first_elem_lst.append(init_list[i][0])
    third_elem_lst.append(init_list[i][2])
print(first_elem_lst, third_elem_lst)