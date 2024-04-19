init_list = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
final_list = []

for tup in init_list:
    final_list.append(tup[1])
print(min(final_list), max(final_list))