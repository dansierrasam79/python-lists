aList = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
total = 0
big_list = []
for lst in aList:
    if sum(lst) > total:
        total = sum(lst)
        big_list = lst
print(total, big_list)