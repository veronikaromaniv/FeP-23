class Payment:
    def __init__(self):
        self.card_details = 0

    def add_card_details(self, balance: int):
        self.card_details = balance

    def verify_payment(self, cart_details: int, cart_items: dict, products: dict):
        total_payment = 0

        for product_id, quantity in cart_items.items():
            if product_id in products:
                product_price = products[product_id]
                total_payment += quantity * product_price

        return cart_details >= total_payment
