init_list = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
element = 1
count = 0
for lst in init_list:
    if element in lst:
        count += 1

print(count)
