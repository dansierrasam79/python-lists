aList = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
char_for_search = 'sdf'
for item in aList:
    if item[0:len(char_for_search)] == char_for_search:
        print(item)