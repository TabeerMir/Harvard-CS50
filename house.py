name = input('what is your name?')

match name:
    case 'harry'| 'hermione'| 'ron':
        print('gryffindor')
    case 'draco':
        print('slytherin')
    case _ :
        print('unknown')
