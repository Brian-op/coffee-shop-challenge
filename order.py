class Order :
    def __init__(self, customer, coffee, price):
        self.customer_name = customer
        self.coffee_name = coffee
        self.coffee_price = price 

        if not isinstance(price, float):
            raise ValueError ("Your price needs to be a float")
        if not (1.0<= price <=10.0):
            raise ValueError("You are not within the right price range")

   
    @property
    def price(self):
        return self.coffee_price
    
    
