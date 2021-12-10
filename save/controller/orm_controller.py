from model.adres import Adress
from model.person import Person


class ORM:
    
    def object_to_file(self, people, path):
        with open(path, 'w', encoding='utf-8') as file:
            for person in people:
                file.write(f'{Person.to_csv()}\n')
        
    def file_to_object(self, path):
        people = []
        with open (path, "r", encoding="utf-8") as file:
            for person in people:
                p = person.split("; ")
                people.append(Person(p[0], p[1], Adress(p[2], p[3], p[4])))
        return people
        
    

if __name__ == '__main__':
    
    orm = ORM()
    a1 = Adress('Krolewska', '00-232', 'Warszawa')
    p1 = Person("Dawid", 'Michalczyk', a1)
    p2 = Person('Jan', 'Kowalski', a1)
    people = [p1, p2]
    orm.object_to_file(people, "people.csv")
    for p in orm.file_to_object("people.csv"):
        print(p, end="")