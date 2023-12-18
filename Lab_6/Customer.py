from Inventory_Subsystem import *
from Order_Process_Subsystem import *
from Payment_Subsystem import *
from Shipment_Subsystem import *
import json


class Customer:
    def __init__(self, order_item):
        self.order_item = order_item

    def place_order(self, order_facade):
        order_facade.process_order(self.order_item)

class OrderFacade:
    def __init__(self):
        self.stock = Stock()
        self.product = Product()
        self.shopping_cart = ShoppingCart()
        self.order = Order()
        self.shipment = Shipment()
        self.shipment_provider = ShipmentProvider()

    def register_customer(self, customer):
        self.customer = customer

    def process_order(self, order_data_path):
        with open(order_data_path, 'r') as file:
            order_data = json.load(file)

        product_id = order_data.get("product_id", "")
        price = order_data.get("price", 0)
        cart_details = order_data.get("cart_details", 0)
        stock_items = order_data.get("stock_items", [])

        for stock_item in stock_items:
            item_id = stock_item.get("item_id", "")
            quantity = stock_item.get("quantity", 0)

            self.stock.update_stock(item_id, quantity)



        self.product.add_product(product_id, price)
        self.shopping_cart.add_item(product_id, order_data.get("quantity", 0))

        if self.shopping_cart.checkout(self.stock.stock_items, cart_details, self.product.products):
            order_id = self.order.create_order(
                self.shopping_cart.cart_items,
                order_data.get("customer_info", {})
            )

            self.shipment.create_shipment(order_id, order_data.get("shipping_address", ""))

            provider_id = order_data.get("provider_id", "")
            provider_info = order_data.get("provider_info", {})

            self.shipment_provider.add_provider(provider_id, provider_info)

            print(f"Product ID: {product_id}, Quantity: {order_data.get('quantity', 0)}, Price: {price}")
        else:
            print("Checkout failed")



