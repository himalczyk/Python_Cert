from adres import Adres
from person import Person

person1_address = Adres('Ulica', '11-123', 'Warszawa')
person1 = Person('Dawid', 'Michalczyk', person1_address)
person2_address = Adres('Street', '12-123', 'City2', )
person2 = Person('Jan', 'Kowal', person2_address)

print(person1)
print(person2)
