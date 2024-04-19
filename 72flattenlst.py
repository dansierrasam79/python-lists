aList = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
final_list = []
int_type = type(10)
lst_type = type([10])
for item in aList:
    if type(item) != lst_type:
        final_list.append(item)
    else:
        for element in item:
            final_list.append(element)
print(final_list)