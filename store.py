import products

class Store:
    def __init__(self, product_list):
        self.product_list = product_list
        
    def add_product(self, product):
        self.product_list.append(product)
        
    def remove_product(self, product):
        self.product_list.pop(product)
    
    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.quantity
        return total_quantity
            
    def get_all_products(self) -> list:
        products = []
        for product in self.product_list:
            if product.active:
                products.append(product)
        return products
    
    def order(self, shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.price * quantity
            product.quantity = product.quantity - quantity
        
        return total_price
            