word_list = ['be','have','do','say','get','make','go','know','take','see','come','think','look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
first_letter = 'c'
final_list = []
for word in word_list:
    for char in word:
        if word[0] == first_letter and word not in final_list:
            final_list.append(word)
print(final_list)