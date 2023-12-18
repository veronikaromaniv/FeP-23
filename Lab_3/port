from abc import ABC, abstractmethod
import haversine as hs

from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from ship import Ship

class IPort(ABC):
    @abstractmethod
    def incoming_ship(self, ship: Ship):
        pass

    @abstractmethod
    def outgoing_ship(self, ship: Ship):
        pass

class Port(IPort):
    def __init__(self, port_id: str, latitude: float, longitude: float):
        self.id = port_id
        self.containers = {
            "basic_container": [],
            "heavy_container": [],
            "refrigerated_container": [],
            "liquid_container": []
        }
        self.ship_history = []
        self.current_ships = []
        self.latitude = latitude
        self.longitude = longitude

    def get_distance(self, port) -> float:
        dist = hs.haversine((self.latitude, self.longitude), (port.latitude, port.longitude))
        return dist

    def incoming_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship not in self.current_ships:
            self.current_ships.append(ship)
            return True
        return False

    def outgoing_ship(self, ship: Ship) -> bool:
        if isinstance(ship, Ship) and ship in self.current_ships:
            self.current_ships.remove(ship)
            self.ship_history.append(ship)
            return True
        return False

    def add_container(self, container):
        if isinstance(container, BasicContainer):
            self.containers["basic_container"].append(container)
        elif isinstance(container, HeavyContainer):
            self.containers["heavy_container"].append(container)
        elif isinstance(container, RefrigeratedContainer):
            self.containers["refrigerated_container"].append(container)
        elif isinstance(container, LiquidContainer):
            self.containers["liquid_container"].append(container)
