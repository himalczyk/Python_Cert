import datetime

class User():
    
    def __init__(self, first_name: str, last_name: str, gender: bool, year_birth: int):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        if datetime.date.today().year < year_birth:
            self.year_birth = None
        else:
            self.year_birth = year_birth
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, gender: {'M' if self.gender else 'K'}, age: {self.calculate_age()}"
        
    def calculate_age(self):
        return datetime.date.today().year - self.year_birth if self.year_birth != None else 'n/a'
    
person1 = User('Dawid', 'Michalczyk', True, 1996)
person2 = User('Agata', 'Kowalska', False, 1984)
print(person1)
print(person2)
setattr(person2, "year_birth", 1990)
setattr(person1, "year_birth", 2022)
print(person1)
print(person2)
    