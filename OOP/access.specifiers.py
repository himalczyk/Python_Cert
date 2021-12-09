class Example:
    
    def __init__(self, normal, private, strong_private):
        self.normal = normal
        self._private = private
        self.__strong_private = strong_private
        
    def get_strong_private(self):
        return self.__strong_private
    
    def set_strong_private(self, strong_private):
        self.__strong_private = strong_private
        
e = Example(1,2,3)
print(e.normal)
print(e._private)
