
'''
x= int(input('whats x?'))

if x%2 == 0:
    print ('even')
else:
    print ('odd')
'''

def main():
    x= int(input('whats x?'))
    if is_even(x):
        print ('even')
    else:
        print('odd')

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
main()