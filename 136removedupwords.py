init_list = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises']
final_list = []
for word in init_list:
    count = 0
    for word2 in init_list:
        if word == word2:
            count += 1
    if count == 1:
        final_list.append(word)
    else:
        if word not in final_list:
            final_list.append(word)
print(final_list)