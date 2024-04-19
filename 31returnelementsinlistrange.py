aList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 90, 70, 80]
upperRange = 35
lowerRange = 90
count = 0
for num in aList:
    if num >= upperRange and num <= lowerRange:
        count += 1
print("Number of elements between", upperRange, " and ", lowerRange, "is", count)