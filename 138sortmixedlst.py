init_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
num_list = []
word_list = []
final_list = []
for item in init_list:
    if type(item) == type(1):
        num_list.append(item)
for item in init_list:
    if type(item) == type("hello"):
        word_list.append(item)
for num in sorted(num_list):
    final_list.append(num)
for word in sorted(word_list):
    final_list.append(word)
print(final_list)