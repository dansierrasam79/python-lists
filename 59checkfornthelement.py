aList = ["danny", "nutan", "mark", "swapan"]
def checkfornthelement(n):
    if n <= len(aList):
        return True
    else:
        return False

if __name__ == "__main__":
    print(checkfornthelement(10))
    print(checkfornthelement(1))