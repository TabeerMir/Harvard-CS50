def main():
    x = get_int('whats x?')
    print(f'x is {x}')


def get_int(prompt):
    while True:   
        try:
            x = int(input(prompt))
        except ValueError:
            print('x not integer') #pass would also handle error
        else:
            return x #return breaks and returns but break onlt breaks out of loop