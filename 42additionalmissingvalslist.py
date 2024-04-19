aList = ['a','b','c','d', 'e']
bList = ['d','e','f','g','h']

missinglist = []
addlist = []

for bet in aList:
    if bet not in bList:
        missinglist.append(bet)

for bet2 in bList:
    if bet2 not in aList:
        addlist.append(bet2)

print(missinglist, addlist)