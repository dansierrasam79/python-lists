primenolist = []
def findprimenos(n):
    for i in range(2,n):
        for j in range(2,n):
            if i*j in primenolist:
                primenolist.remove(i*j)

if __name__ == "__main__":
    n = 100
    for i in range(0, n+1):
        primenolist.append(i)
    findprimenos(n)
    print(primenolist)