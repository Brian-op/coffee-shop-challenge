from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
       return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise AttributeError("You cannot change coffee name if already set")
        
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        
        self._name = name

       
    def orders(self):
       return[order for order in Order.all if order.coffee == self]
    
    def customers(self):
       return list(set(order.customer for order in self.orders()))


    def order_numbers(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)
        