class Person:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
    def to_csv(self):
        return f"{self.first_name}; {self.last_name}; {self.address.to_csv()}"
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.address}"
class Address:
    def __init__(self, street, postal_code, city):
        self.street = street
        self.postal_code = postal_code
        self.city = city
    def to_csv(self):
        return f"{self.street}; {self.postal_code}; {self.city}"
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

p = Person("Michał", "Kru", Address("X","X","X"))
# p = None
if __debug__:
    assert p.address != None, 'adres obiektu person nie może być None'