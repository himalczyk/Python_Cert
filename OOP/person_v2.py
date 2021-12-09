import datetime

class Person():
    
    def __init__(self, first_name: str, last_name: str, gender: bool, year_birth: int):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_gender(gender)
        self.set_year_birth(year_birth)
    
    def __str__(self):
        return f"{self.get_first_name()} {self.get_last_name()}, gender: {'M' if self.get_gender() else 'K'}, age: {self.calculate_age()}"
        
    def calculate_age(self):
        return datetime.date.today().year - self.__year_birth if self.__year_birth != None else 'n/a'
    
    def set_first_name(self, first_name: str):
        if first_name.isalnum():
            self.__first_name = first_name
        else:
            print('First Name cannot be empty')
    
    def get_first_name(self):
        return self.__first_name
    
    def set_last_name(self, last_name: str):
        if last_name.isalnum():
            self.__last_name = last_name
        else:
            print('Last Name cannot be empty')
            
    def get_last_name(self):
        return self.__last_name
    
    def set_gender(self, gender: bool):
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_year_birth(self, year_birth: int):
        if datetime.date.today().year < year_birth:
            self.__year_birth = None
        else:
            self.__year_birth = year_birth
            
    def get_year_birth(self):
        return self.__year_birth
    
person1 = Person('Dawid', 'Michalczyk', True, 1995)
# print(person1)
# print(person2)
# setattr(person2, "year_birth", 1990)
# setattr(person1, "year_birth", 2022)
# print(person1)
# print(person2)
print(person1)