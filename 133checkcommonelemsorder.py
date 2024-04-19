init_list = ['red', 'green', 'black', 'orange']
init_list2 =['red', 'pink', 'green', 'white', 'black']
init_list3 = ['white', 'orange', 'pink', 'black']

init_list12 = []
init_list21 = []
init_list13 = []
init_list31 = []
init_list23 = []
init_list32 = []

for item in init_list2:
    if item in init_list:
        init_list12.append(item)

for item in init_list:
    if item in init_list2:
        init_list21.append(item)

if init_list12 == init_list21:
    print(True)
else:
    print(False)
    
for item in init_list3:
    if item in init_list:
        init_list13.append(item)

for item in init_list:
    if item in init_list3:
        init_list31.append(item)

if init_list13 == init_list31:
    print(True)
else:
    print(False)

for item in init_list3:
    if item in init_list2:
        init_list23.append(item)

for item in init_list2:
    if item in init_list3:
        init_list32.append(item)

if init_list23 == init_list32:
    print(True)
else:
    print(False)
