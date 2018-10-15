import sys

if sys.argv[1]:
    msg = 'Bonjour tout le monde {}'.format(sys.argv[1])
    print('Message is: ', msg)
    print('The 0th arg: ' + str(sys.argv[0]))
    print('The args are: ' + str(sys.argv))
    exit(0)
exit(1)
