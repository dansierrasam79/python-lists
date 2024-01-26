aList = [1,2,3,4,5,6,7,8,9,10,3,5,6,7]
noduplist = []
for item in aList:
    if item not in noduplist:
        noduplist.append(item)
print(noduplist)