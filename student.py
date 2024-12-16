class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError ('missing name')
        if house not in ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']:
            raise ValueError('invalid hoouse')
        self.name = name 
        self.house = house
    
    def __str__(self):
        return f'{self.name} from{self.house}'
    
    #getter - gets attribute for class
    @property
    def house(self):
        return self._house
    
    #setter - function that sets a value for a class
    @house.setter
    def house(self, house):
        if house not in ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']:
            raise ValueError('invalid house')
        self._house = house
    

def main():
    student = get_student()
    print(student)


def get_student():
    name = input ('Name:')
    house = input('House:')
    return Student(name, house)

if __name__ == " __main__":
    main()

