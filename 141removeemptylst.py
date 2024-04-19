init_list = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
final_list = []

for lst in init_list:
    if len(lst) != 0:
        final_list.append(lst)
print(final_list)