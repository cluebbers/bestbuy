class Product:
    def __init__(self, name, price, quantity):
        """
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.
        """
        if not name:
            raise ValueError("Enter a name")
        else:
            self.name = name

        if price < 0 or not isinstance(price, (int, float)):
            raise ValueError("Price should be a positive number")
        else:
            self.price = price

        if quantity < 0:
            raise ValueError("Quantity has to be positive!")
        else:
            self.quantity = quantity

        self.active = True

    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        Returns the quantity (int).
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Setter function for quantity. If quantity reaches 0, deactivates the product.
        """
        if quantity < 0:
            raise ValueError("Quantity has to be positive!")
        self.quantity = quantity
        if quantity == 0:
            self.active = False
        else:
            self.active = True

    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self):
        """
        Prints a string that represents the product, for example:
        "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.
        """
        if quantity > self.quantity:
            raise ValueError(f"There are only {self.quantity} left!")
        else:
            self.set_quantity(self.quantity - quantity)
        return self.price * quantity
