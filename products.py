class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Enter a name")
        else: 
            self.name = name
        
        if price < 0 or price is type(str):
            raise ValueError("Price should be a positive number")
        else:
            self.price = price
        
        if quantity < 0:
            raise ValueError("Quantity has to be positive!")
        else:
            self.quantity = quantity
            
        self.active = True
    
    def get_quantity(self) -> int:
        return self.quantity
    
    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity == 0:
            self.active = False
    
    def is_active(self) -> bool:
        return self.active
    
    def activate(self):
        self.active = True
        
    def deactivate(self):
        self.active = False
        
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")
        
    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            raise ValueError(f"There are only {self.quantity} left!")
        else: 
            self.quantity = self.quantity - quantity
        return self.price * quantity
    