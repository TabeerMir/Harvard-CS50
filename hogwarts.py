#dictionaries


'''students = {
    'hermione': 'gryffindor',
    'harry': 'gryffindor',
    'ron':'gryffindor',
    'draco': ' slytherin'
}

for student in students:
    print (student, students[student], sep ='-')'''


#databases

students =[
    {'name':'hermione', 'house': 'gryffindor', 'patronus':'otter'},
    {'name': 'harry', 'house':'gryffindor', 'patronus':'stag'}
]

for student in students:
    print(student['name'], student['house'], student['patronus'])

