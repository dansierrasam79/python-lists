init_list = [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
final_dict = {}
for lst in init_list:
    count = 0
    for lst2 in init_list:
        if lst == lst2:
            count += 1
    final_dict[tuple(lst)] = count
print(final_dict)
        
