class Trainer:
    def __init__(self, trainer_name):
        self.trainer_name = trainer_name
        
    def get_name(self):
        return self.trainer_name

class Software(Trainer):

    def __init__(self, technology,version, price):
        self.technology = technology
        self.price = price
        self.version = version
        
    def __str__(self):
        return f"{self.technology} {self.version} {self.price}"
        
class Course(Software):
    def __init__(self, name, date, technology, version, price):
        super().__init__(technology, version, price) #calling constructor from superclass must be in first line in the subclass concstructor
        self.name = name
        self.date = date
        
    def __str__(self):
        return f"{self.name} {self.date} {super().__str__()} {super().get_name()}"
    

# software = Software("Windows", "11", 1500)
course = Course("Python", "06-10.12.2021", "PY", "Daily", 3500)
course.trainer_name = "DM"
print(course.__str__())