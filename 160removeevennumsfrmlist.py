init_list = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
final_list = []
count = 0
for num in init_list:
    if num % 2 == 0 and count < 4:
        print("Even number")
        count += 1
    else:
        final_list.append(num)
print(final_list)