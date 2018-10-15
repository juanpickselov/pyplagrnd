def reverse_it(my_string):
    myLen = len(my_string)
    zeroBasedLen = myLen - 1
    newString = ''
    for aChar in range(myLen):
        newString += my_string[zeroBasedLen - aChar]
    print(newString)


def reverse_text(text_to_reverse):
    print(text_to_reverse[::-1])
