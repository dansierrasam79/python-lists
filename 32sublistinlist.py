aList = [1,2,3,[4,5],6,7,[8,9,10]]

for item in aList:
    if type(item) == type([0,0,0]):
        print("Sublist exists")
        break;