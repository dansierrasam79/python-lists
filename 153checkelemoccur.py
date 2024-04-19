init_list = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
final_list = []
three_count = 0
zero_count = 0
eight_count = 0
for num in init_list:
    if num == 3:
        three_count += 1
    if num == 0:
        zero_count += 1
    if num == 8:
        eight_count += 1

if three_count >= 4:
    print(True)
else:
    print(False)
if zero_count >= 5:
    print(True)
else:
    print(False)
if eight_count >= 3:
    print(True)
else:
    print(False)