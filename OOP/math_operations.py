class MathOperations():
    
    def __init__(self, number1: float, number2: float):
        self.__set_number1(number1)
        self.__set_number2(number2)
    
    def __set_number1(self, number1):
        self.__number1 = abs(number1)
    def __get_number1(self):
        return self.__number1
    def __set_number2(self, number2):
        self.__number2 = abs(number2)
    def __get_number2(self):
        return self.__number2
    number1 = property(__get_number1, __set_number1)
    number2 = property(__get_number2, __set_number2)
    
operation = MathOperations(1, 3)
print(operation.number1, operation.number2)
operation.number1 = 10
operation.number2 = 15
print(operation.number1, operation.number2)