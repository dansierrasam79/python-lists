aList = ['p','q']
n = 5
fList = []

for i in range(1,n+1):
    for item in aList:
        myString = ""
        myString = item + str(i)
        fList.append(myString)
print(fList)
