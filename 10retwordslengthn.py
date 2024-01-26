aList = ["Daniel", "Joseph", "Mo", "Sahu", "Borat"]
finalList = []
n = 2
for item in aList:
    if len(item) > n:
        finalList.append(item)
print(finalList)