class Customer :
    def __init__(self, name):
        self._customer_name = name

    @property
    def name (self):
        return self._name 
    
    @name.setter
    def name (self, name):
        if len(name) > 15: 
         raise TypeError("Characters should not exceed 15")
        elif not isinstance (name, str):
           raise TypeError("Name must be a string")
        else  :
           return self._name 