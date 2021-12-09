class Employee:
    def __init__(self, first_name, last_name, salary):
        self.__set_first_name(first_name)
        self.__set_last_name(last_name)
        self.__set_salary(salary)
        
    def __get_first_name(self):
        return self.__first_name
    
    def __set_first_name(self, first_name):
        self.__first_name = first_name
    
    def __get_last_name(self):
        return self.__last_name
    
    def __set_last_name(self, last_name):
        self.__last_name = last_name
        
    def __get_salary(self):
        return self.__salary
    
    def __set_salary(self, salary):
        self.__salary = salary
    
    first_name = property(__get_first_name, __set_first_name)
    last_name = property(__get_last_name, __set_last_name)
    salary = property(__get_salary, __set_salary)
    
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.first_name} {self.last_name}, {self.salary}"
    
class Manager(Employee):
    def __init__(self, first_name, last_name, salary, role, list_employees: set = []):
        super().__init__(first_name, last_name, salary)
        self.list_employees = list_employees
        self.role = role
        
    def __str__(self):
        return f"{super().__str__()}; role: {self.role}; employees = {[empl.__str__() for empl in self.list_employees]}"
    
    def get_empl_by_index(self, index):
        return self.list_employees[index]
    def add_empl(self, employee):
        self.list_employees.append(employee)
    def del_empl_index(self, index):
        self.list_employees.remove(index)
        
class Company:
    def __init__(self, employees):
        self.employees = employees
    def get_employess(self):
        for empl in self.employees:
            print(empl)
    
person1 = Employee('Dawid', 'Michalczyk', 3000)
person2 = Employee('Jan', 'Michalczyk', 1234)
person3 = Employee('Michal', 'Michalczyk', 12345)
person4 = Employee('Kuba', 'Michalczyk', 123456)

manager1 = Manager('ManDawid', 'ManMichalczyk', 4000, 'Admin', [person1, person2, person3])
manager2 = Manager('ManKuba', 'ManMichalczyk', 5000, 'AdminIT', [person4])
# print(person1)
# print(manager1)
# print(manager1.get_empl_by_index(0))
# manager1.del_empl_index(0)
# print(manager1) #deletion
# manager1.add_empl(person1)
# print(manager1) #addition
company = Company([person1, person2, person3, person4, manager1, manager2])
company.get_employess()