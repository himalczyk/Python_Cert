import datetime
from typing import Type
import traceback

class BirthDateError(Exception):
    def __init__(self, mesg):
        self.__mesg=mesg
    def __str__(self):
        return self.__mesg

class NoValueError(Exception):
    def __init__(self, mesg):
        self.__mesg=mesg
    def __str__(self):
        return self.__mesg


class Person:
    def __init__(self, name: str, last_name: str, gender: bool, birth_year: int):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_gender(gender)
        self.set_birth_year(birth_year)
    def get_name(self):
        return self.__name
    def get_last_name(self):
        return self.__last_name
    def get_gender(self):
        return self.__gender
    def get_birth_year(self):
        return self.__birth_year
    def set_name(self, name : str):
        try:
            self.__name = name
            if not name.isalnum():
                raise NoValueError("imię nie może być puste")
        except NoValueError as e:
            print(e)
            # traceback.print_exc() - informacja o błędzie taka jak na konsoli
            self.__name = 'anonim'
    def set_last_name(self, last_name : str):
        try:
            self.__last_name = last_name
            if not last_name.isalnum():
                raise TypeError("nazwisko nie może być puste")
        except TypeError as e:
            print(e)
            # traceback.print_exc() - informacja o błędzie taka jak na konsoli
            self.__last_name = 'anonim'
    def set_gender(self, gender : bool):
        self.__gender = gender
    def set_birth_year(self, birth_year : int):
        try:
            self.__birth_year = birth_year
            if datetime.date.today().year < birth_year or birth_year <= 0:
                raise BirthDateError("nieprawidłowa data")
        except BirthDateError as e:
            print(e)
            self.__birth_year = None
    def how_many_years(self):
        return date.today().year - self.get_birth_year() if self.get_birth_year() != None else 'B/D'
    def output_format(self):
        return f"{self.get_name()}; {self.get_last_name()}; {self.get_gender()}; {self.get_birth_year()}"
    def __str__(self):
        return f"{self.get_name()} {self.get_last_name()}, płeć: {'M' if self.get_gender() else 'K'}, wiek: {self.how_many_years()} lat"
    name = property(get_name,set_name)
    last_name = property(get_last_name, set_last_name)
    gender = property(get_gender,set_gender)
    birth_year = property(get_birth_year, set_birth_year)

p = Person("","", True, 2022)
print(p)