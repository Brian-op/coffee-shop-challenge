from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
       return self._name
    
    @name.setter
    def name (self, name):
       
       if len(name) < 3 :
           raise TypeError("Name must be more than 3 characteres long")
       
       self._name = name

       if not isinstance (name, str):
           raise TypeError("Coffee name must be a string")
       
       if hasattr(self,"_name"):
           raise ValueError("You cannot change coffee name if already set")
         
       
    def orders(self):
       return[order for order in Order.all if order.coffee == self]
    
    def customers(self):
       return list(set(order.customers for order in self.orders()))

    
        