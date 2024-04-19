Colors1 = ["red", "orange", "green", "blue", "white"] 
Colors2 = ["black", "yellow", "green", "blue"]
Colors2missing = []
Colors1missing = []
for color in Colors2:
    if color not in Colors1:
        Colors2missing.append(color)

for color in Colors1:
    if color not in Colors2:
        Colors1missing.append(color)

print(Colors1missing, Colors2missing)