def reverse_it():
    myString = "honda accord"
    myLen = len(myString)
    zeroBasedLen = myLen - 1
    newString = ''
    for aChar in range(myLen):
        newString+=myString[zeroBasedLen - aChar]
    print(newString)

def reverse_text():
    the_string = "honda accord"
    the_string_list = list(the_string)
    print(''.join(the_string_list[::-1]))
