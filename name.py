import sys

if len(sys.argv)<2:
    print('too few arguments')
'''elif len(sys.argv)>2:
    print('too many arguments')
else:'''
    
print('hello, my name is', sys.argv[1], sys.argv[2])

for name in sys.argv[1:]: #slice from 1 to give arguments at position 2 until the end
    print('hello to', name)