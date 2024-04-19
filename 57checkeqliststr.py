aList = ["When", " Harry", " met", " Sally"]
aString = "When Harry met Sally"
bString = ""
for word in aList:
    bString += word

if aString == bString:
    print("Same")
else:
    print("Not same")