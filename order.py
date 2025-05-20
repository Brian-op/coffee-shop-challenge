class Order :
    all = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all.append(self) 

        if not isinstance(price, float):
            raise ValueError ("Your price needs to be a float")
        if not (1.0<= price <=10.0):
            raise ValueError("You are not within the right price range")

   
    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer
        
    @property
    def coffee(self):
        return self._coffee
    

