class Point2D:
    def __init__(self, x, y):
        self.__set_x(x)
        self.__set_y(y)
        
    def __get_x(self):
        return self.__x
    def __get_y(self):
        return self.__y
    def __set_x(self, x):
        self.__x = x
    def __set_y(self, y):
        self.__y = y
        
    def __str__(self) -> str:
        return F"x = {self.__get_x} y = {self.__get_y}"
    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)
    
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.__set_z(z)
        
    def __get_z(self):
        return self.__z
    def __set_z(self, z):
        self.__z = z
        
    def __str__(self):
        return f"{super().__str__()} z = {self.__get_z()}"
    z = property(__get_z, __set_z)