init_list = ['red', 'black', 'white', 'green', 'orange']
search_string = 'ack'
for word in init_list:
	if search_string in word:
		print(word, True)