class Stock:
    def __init__(self):
        self.stock_items = {}

    def select_stock_item(self, product_id):
        return product_id in self.stock_items

    def update_stock(self, product_id, quantity : int):
        self.stock_items[product_id] = quantity


class Product:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, price: int):
        self.products[product_id] = price

    def update_product(self, product_id, price: int):
        if product_id in self.products:
            self.products[product_id] = price
