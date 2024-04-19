init_list = ['red', 'green', 'blue', 'white', 'black', 'orange']
init_list2 = ['white', 'orange']
final_list = []
for item in init_list:
    if item not in init_list2:
        final_list.append(item)
print(final_list)