init_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
total = 0
total2 = 0
total3 = 0
for i in range(0, len(init_list)):
    total += init_list[i][0]
    total2 += init_list[i][1]
    total3 += init_list[i][3]
print(total, total2, total3)