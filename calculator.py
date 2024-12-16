'''x=float(input('pick a number '))
y=float(input('pick another number' ))

#if int isnt used it will always be a string so x+y would concatinate

z = round(x+y)

print (f'{x}+{y}= {z:,}')

a =round(x/y, 2)
print (f'{x}/{y}= {a:,}')'''

def main():
    x = int(input('pick a number'))
    print(f'{x} squared is', square(x))

def square(n):
    return n*n
#you could also do n**2 or pow(n,2)

if __name__ == ' __main__':
    main()