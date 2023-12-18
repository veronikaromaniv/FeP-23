class Shipment:
    def __init__(self):
        self.shipments = {}

    def create_shipment(self, order_id, shipping_address):
        self.shipments[order_id] = {"shipping_address": shipping_address, "providers": {}}

    def add_provider(self, order_id, provider_id, provider_info):
        if order_id in self.shipments:
            self.shipments[order_id]["providers"][provider_id] = provider_info

class ShipmentProvider:
    def __init__(self):
        self.providers = {}

    def add_provider(self, provider_id, provider_info):
        self.providers[provider_id] = provider_info

    def modify_provider(self, provider_id, new_info):
        if provider_id in self.providers:
            self.providers[provider_id].update(new_info)
