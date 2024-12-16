'''names = []

for i in range(3):
    names.append(input('whats your name?'))

for name in sorted(names):
    print(f'hello, {name}')'''

'''name = input('whats your name?')


file = open('names.txt','a') #a=append, w=write which writes over previous names
file.write(f'{name}\n')
file.close()

with open('names.txt','a') as file:
    file.write(f'{name}\n')'''

names = []
with open('names.txt', 'r') as file: #r = read
    for line in file:
        names.append(line.rstrip()) 
    
    for name in sorted(names):
        print(f'hello,{name}')

