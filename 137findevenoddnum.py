init_list = [1, 3, 5, 7, 4, 1, 6, 8]
final_list = []
for num in init_list:
    if num % 2 == 0:
        final_list.append(num)
        break;
for num in init_list:
    if num % 2 != 0:
        final_list.append(num)
        break;    
print(final_list)
