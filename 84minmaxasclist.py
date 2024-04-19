aList = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
final_list = []
for num in aList:
    final_list.append(round(num))
print("minimum value", min(final_list))
print("maximum value", max(final_list))
for i in range(0,len(final_list)):
    new_val = 0
    new_val = final_list[i]*5
    final_list[i] = new_val
final_list.sort()
print("list in ascending order", final_list)
