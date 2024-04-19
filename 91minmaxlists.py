init_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
min_lst_val = 999
max_lst_val = 0
min_lst = []
max_lst = []
for lst in init_list:
    if len(lst) < min_lst_val:
        min_lst_val = len(lst)
        min_lst = lst
    if len(lst) > max_lst_val:
        max_lst_val = len(lst)
        max_lst = lst

print(min_lst, min_lst_val)
print(max_lst, max_lst_val)
    
