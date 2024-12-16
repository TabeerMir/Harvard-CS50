'''n=3
while n !=0:
    print('meow')
    n=n-1 #can also be written as n-=1


for i in range (3):
    print('pur')

print ('hiss\n'*3, end = '')


while True:
    x = int(input('number?'))
    if x > 0:
        break

for _ in range (x):
    print ('woof')'''


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input('number?'))
        if n > 0:
            return n

def meow(n):
    for i in range (n):
        print('meow')

main()