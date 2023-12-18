from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4
from containers import HeavyContainer, BasicContainer, RefrigeratedContainer, LiquidContainer


@dataclass
class ConfigShip:
    total_weight_capacity: int
    max_number_of_all_containers: int
    maxNumberOfHeavyContainers: int
    maxNumberOfRefrigeratedContainers: int
    maxNumberOfLiquidContainers: int
    fuelConsumptionPerKM: float


class IShip(ABC):

    @abstractmethod
    def sail_to(self, port) -> bool:
        pass

    @abstractmethod
    def refuel(self, amount_of_fuel: float) -> None:
        pass

    @abstractmethod
    def load(self, container) -> bool:
        pass

    @abstractmethod
    def unload(self, container) -> bool:
        pass


class Ship(IShip):
    """Ship implementation"""

    FUEL_CAPACITY = 1000

    def __init__(self, port, ship_config: ConfigShip, fuel: float = FUEL_CAPACITY) -> None:
        self.id = uuid4()
        self.fuel = fuel
        self.port = port
        self.configs = ship_config
        self.containers = []

    def get_current_containers(self) -> list:
        return self.containers

    def sail_to(self, port) -> bool:
        if self.fuel > 0:
            distance = self.port.get_distance(port)
            fuel_needed = distance * self.configs.fuelConsumptionPerKM
            if self.fuel >= fuel_needed:
                self.fuel -= fuel_needed
                self.port = port
                return True
        print(f"Ship {self.id} does not have enough fuel to sail to {port.id}.")
        return False

    def refuel(self, amount_of_fuel: float):
        self.fuel += amount_of_fuel

    def load(self, container) -> bool:
        if len(self.containers) < self.configs.max_number_of_all_containers:
            self.containers.append(container)
            return True
        return False

    def unload(self, container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False
