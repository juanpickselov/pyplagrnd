myString = "accord"
myLen = len(myString)
zeroBasedLen = myLen - 1
newString = ''
for aChar in range(myLen):
    newString+=myString[zeroBasedLen - aChar]
print(newString)
