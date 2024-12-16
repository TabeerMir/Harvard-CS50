def hello():
    name = input('what is your full name? ').strip().title()
    #get user name

    first,last = name.split(' ')
    #split name into first and last name

    '''name = name.strip().title()'''
    #this removes whitespace from string and capitalise

    '''name = name.capitalize()'''
    #capitalise name

    print(f'hello, {name}, i will call you {first}')
    #say hello to use
    #sep is a seperator and is ' ' by default but you can change this by defining sep = something else
    #end is by default \n which starts a new line but you could get rid of this by defining end as = ' '
    #putting a backslash in front of quote marks will allow you to print quote marks


    '''print (f'hello {name}')'''



hello()


def age():
    age = int(input('what is your age in numbers? '))
    print(age,'is very young')

age()


