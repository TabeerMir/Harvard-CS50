

students = []

with open ('students.csv') as file:
    for line in file:
        '''row=line.rstrip().split(',')
        print(f'{row[0]} is in {row[1]}')'''
        name, house =line.rstrip().split(',')
        '''students.append(f'{name} is in {house}')'''
        student ={}
        student['name']= name
        student['house'] = house
        students.append(student)

'''for student in sorted (students):
    print(student)'''

def get_name(student):
    return student['name']

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")