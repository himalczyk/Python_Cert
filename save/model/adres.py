class Adress:
    
    def __init__(self, street, postal_code, city):
        self.street = street
        self.postal_code = postal_code
        self.city = city
        
    def to_csv(self):
        return f"{self.street}; {self.postal_code}; {self.city}"
    
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    