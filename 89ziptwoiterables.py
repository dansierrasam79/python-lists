first_list = [[1, 3], [5, 7], [9, 11]]
second_list = [[2, 4], [6, 8], [10, 12, 14]]
temp_list = []
final_list = []

for i in range(0,len(first_list)):
    temp_list = zip(first_list[i],second_list[i])
    final_list.append(list(temp_list))
print(final_list)
