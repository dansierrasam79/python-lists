aList = [{},{},{}]
bList = [{1,2},{},{}]
aList_count = 0
bList_count = 0
for dict in aList:
    if len(dict) > 0:
        aList_count += 1
for dict in bList:
    if len(dict) > 0:
        bList_count += 1

if aList_count > 0:
    print("aList is NOT empty")
else:
    print("aList is EMPTY")

if bList_count > 0:
    print("bList is NOT empty")
else:
    print("bList is EMPTY")