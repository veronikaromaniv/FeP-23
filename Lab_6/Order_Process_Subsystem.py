from Payment_Subsystem import *


class ShoppingCart:
    def __init__(self):
        self.cart_items = {}

    def add_item(self, product_id, quantity):
        self.cart_items[product_id] = quantity

    def update_quantity(self, product_id, new_quantity):
        if product_id in self.cart_items:
            self.cart_items[product_id] = new_quantity

    def checkout(self, stock_items: dict, cart_details: int, products: dict):
        payment = Payment()

        payment.add_card_details(cart_details)
        if payment.verify_payment(cart_details, self.cart_items, products) and self.check_stock_quantity(stock_items):
            return True
        else:
            return False

    def check_stock_quantity(self, stock_items: dict):
        for product_id, cart_quantity in self.cart_items.items():
            if product_id not in stock_items:
                return False

            stock_quantity = stock_items[product_id]

            if cart_quantity > stock_quantity:
                return False

        return True

class Order:
    def __init__(self):
        self.orders = {}
        self.next_order_id = 1

    def create_order(self, cart, customer_info):
        order_id = self.next_order_id
        self.next_order_id += 1
        order_data = {
            "cart": cart,
            "customer_info": customer_info,

        }
        self.orders[order_id] = order_data
        return order_id

    def edit_order(self, order_id, new_info):
        if order_id in self.orders:
            self.orders[order_id].update(new_info)
            return True
        else:
            return False
