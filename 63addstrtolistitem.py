aList = [1,2,3,4,5]
aString = 'emp'
for i in range(0, len(aList)):
    finalString = ""
    finalString = aString + str(aList[i])
    aList[i] = finalString
print(aList)