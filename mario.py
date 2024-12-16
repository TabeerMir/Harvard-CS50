def vert():
    print_column(3)

def print_column(height):
    for i in range(height):
        print('#')
    
vert()

def horiz():
    print_row(4)

def print_row(width):
    print('?'* width)

horiz()

def block():
    print_square(3)

def print_square(size): 
    for i in range (size): # for each row in square
        for j in range (size):#for each brick in row
            print('#', end ='')
        print()
    
block()