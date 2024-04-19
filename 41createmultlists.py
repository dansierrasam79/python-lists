finalList = []
templist = []
count = 0
for i in range(0,101):
    if i % 10 != 0:
        templist.append(i)
        count += 1
    else:
        templist.append(i)
        finalList.append(templist)
        count = 0
        templist = []
print(finalList)