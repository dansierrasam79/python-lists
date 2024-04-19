init_list = [2, 4, 7, 0, 5, 8]
init_list2 = [3, 3, -1, 7]
final_list = []

diff = len(init_list) - len(init_list2)
print(diff)

for i in range(2):
    init_list2.append(0)
print(init_list2)

for j in range(0, len(init_list)):
    final_list.append(init_list[j] + init_list2[j])
print(final_list)