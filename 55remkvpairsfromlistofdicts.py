aList = [{"name":"Dan", "age":45}, {"name":"Nutan", "age":70},{"name":"Mark","age":54}]

for dict in aList:
    dict.pop("name")

print(aList)