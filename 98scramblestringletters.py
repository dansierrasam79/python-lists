from random import shuffle
init_list = ['Python', 'list', 'exercises', 'practice', 'solution']
final_list = []
el = []
for elem in init_list:
	final_el = ""
	el = list(elem)
	shuffle(el)
	final_el = ''.join(el)
	final_list.append(final_el)
print(final_list)