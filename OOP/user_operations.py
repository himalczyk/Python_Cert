class User():
    user_id = 1
    
    def __init__(self, first_name: str, last_name: str, age: int, gender: bool, address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address
        
    def __str__(self): #representation class
        return f"{self.first_name} {self.last_name} {self.age} {self.gender} {self.address}"
    
    def increment_user_id(self):
        self.user_id += 1
        
    def set_user_id(self, user_id):
        self.user_id = user_id
        
    def get_user_id(self):
        return self.user_id
    
user1 = User('Dawid', 'Michalczyk', 25, True, 'Warszawa')
print(user1)
setattr(user1, "first_name", "Jan")
getattr(user1, "first_name")

# print(User.__name__)
# print(User.__dict__)
# print(User.__module__)
# print(User.__bases__)
# print(User.__doc__)

# user1 = User() #create new object (instantiate) - get access to all fields, variables and class methods
# user1.increment_user_id()
# print(user1.user_id)