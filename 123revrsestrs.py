init_list = ['Red', 'Green', 'Blue', 'White', 'Black']
final_list = []
for word in init_list:
	word_len = len(word)
	final_list.append(word[::-1])
print(final_list)