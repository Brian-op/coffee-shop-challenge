class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
       return self._name
    
    @name.setter
    def name (self, name):
       if len(name) < 3 :
           return TypeError("Name must be more than 3 characteres long")
       elif not isinstance (name, str):
           return TypeError("Coffee name must be a string")
       else :
           return self._name
        
        