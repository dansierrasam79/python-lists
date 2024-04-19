color_name = ["Black", "Red", "Maroon", "Yellow"] 
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
final_list = []
temp_dict = {}
for i in range(0, len(color_name)):
    temp_dict['color name'] = color_name[i]
    temp_dict['color code'] = color_code[i]
    final_list. append(temp_dict)
    temp_dict = {}
print(final_list)