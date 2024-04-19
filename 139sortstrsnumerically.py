init_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
num_list = []
final_list = []
for item in init_list:
    num_list.append(int(item))
for num in sorted(num_list):
    final_list.append(num)
print(final_list)