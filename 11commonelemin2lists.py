aList = [1,2,3,4,5]
bList = [6,7,8,9,10,2,3]

def compLists():
    count = 0
    for item in aList:
        if item in bList:
            count = count + 1
    if count > 0:
        return True
    else:
        return False

print(compLists())