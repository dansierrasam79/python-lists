init_list = ['orange', 'red', 'green', 'blue']
temp_list = []
final_list = []
for i in range(0,len(init_list)):
    temp_list = []
    for j in range(0, init_list.index(init_list[i])+1):
        temp_list.append(init_list[j])
    final_list.append(temp_list)
print(final_list)