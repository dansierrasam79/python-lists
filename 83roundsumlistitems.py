aList = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
final_list = []
final_val = 0
for num in aList:
    final_list.append(round(num))
print(sum(final_list)*len(final_list))
