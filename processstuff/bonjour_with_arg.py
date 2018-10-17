import sys


if len(sys.argv) == 1:
    print('Script ' + sys.argv[0] + ' ran without arguments')

if len(sys.argv) > 1:
    msg = 'Bonjour tout le monde {}'.format(sys.argv[1])
    print('Message is: ', msg)

    print('Script Name (0th arg): ' + str(sys.argv[0]))
    print('The number of arguments: ' + str(len(sys.argv)))
    print('The args are: ' + str(sys.argv))
