init_list = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
init_list2 = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
init_list3 = [['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], ['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
# removes the first item in each sublist
for i in range(0, len(init_list)):
    del init_list[i][0]
print(init_list)
# removes the second item in each sublist
for i in range(0, len(init_list2)):
    del init_list2[i][1]
print(init_list2)
# removes the last item in each sublist
for i in range(0, len(init_list3)):
    del init_list3[i][3]
print(init_list3)