init_list = [1, 1, 2, 3, 3, 4, 4, 5]
final_list = []
for i in range(1,len(init_list)):
    final_list.append((init_list[i-1],init_list[i]))
print(final_list)