from OOP.user_operations import User


from user_operations import User

def compare_objects(object):
    print(isinstance(object, User))
    
user1 = User()
compare_objects(user1)
compare_objects()