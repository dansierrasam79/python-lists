aList = [(5,2), (6,0), (8,4)]
smallest = 999
small_tup = ()
for tup in aList:
    if tup[1] <= smallest:
        smallest = tup[1]
        small_tup = tup
print(small_tup)