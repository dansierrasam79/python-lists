aList = ['abc', 'xyz', 'aba', '1221']
count = 0
for mystr in aList:
    if len(mystr) >= 2 and mystr[0] == mystr[-1]:
        count = count + 1
print(count)