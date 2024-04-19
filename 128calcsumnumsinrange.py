init_list = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
start = 8
stop = 10
final_sum = 0
for i in range(start, stop+1):
	final_sum = final_sum + init_list[i]
print(final_sum)