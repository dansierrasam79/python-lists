init_list = [10, 20, 4, 5, 'b', 70, 'a']
total = 0
g_total = 0
for num in init_list:
    if type(num) == type(1):
        for digit in str(num):
            total = total + int(digit)
        g_total += total
        total = 0
print(g_total)