from abc import ABC, abstractmethod
from uuid import uuid4
from typing import List
import haversine as hs


class ConfigShip:
    def __init__(self, total_weight_capacity, max_number_of_all_containers, maxNumberOfHeavyContainers,
                 maxNumberOfRefrigeratedContainers, maxNumberOfLiquidContainers, fuelConsumptionPerKM):
        self.total_weight_capacity = total_weight_capacity
        self.max_number_of_all_containers = max_number_of_all_containers
        self.maxNumberOfHeavyContainers = maxNumberOfHeavyContainers
        self.maxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers
        self.maxNumberOfLiquidContainers = maxNumberOfLiquidContainers
        self.fuelConsumptionPerKM = fuelConsumptionPerKM


class IShip(ABC):
    @abstractmethod
    def load(self, container) -> bool:
        pass

    @abstractmethod
    def unload(self, container) -> bool:
        pass

    @abstractmethod
    def sail_to(self, port) -> bool:
        pass

    @abstractmethod
    def refuel(self, fuel) -> bool:
        pass


class Ship(IShip):
    def __init__(self, ship_id, port, configs) -> None:
        self.id = ship_id
        self.containers = []
        self.port = port
        self.configs = configs
        self.current_fuel = 0

    def load(self, container) -> bool:
        if len(self.containers) >= self.configs.max_number_of_all_containers:
            return False
        if container.consumption() > 4:
            self.containers.append(container)
            return True
        return False

    def unload(self, container) -> bool:
        if container in self.containers:
            self.containers.remove(container)
            return True
        return False

    def sail_to(self, port) -> bool:
        if port is None:
            return False

        # Calculate the distance based on latitude and longitude
        distance = hs.haversine((self.port.latitude, self.port.longitude),
                                (port.latitude, port.longitude))

        if distance > self.current_fuel / self.configs.fuelConsumptionPerKM:
            return False

        self.port = port
        self.current_fuel -= distance * self.configs.fuelConsumptionPerKM
        return True

    def refuel(self, fuel) -> bool:
        if self.current_fuel + fuel > 100:
            return False
        self.current_fuel += fuel
        return True


class ShipBuilder(ABC):
    @abstractmethod
    def build_ship(self, port) -> Ship:
        pass


class LightWeightShipBuilder(ShipBuilder):
    def build_ship(self, port) -> Ship:
        configs = ConfigShip(total_weight_capacity=50000, max_number_of_all_containers=20,
                             maxNumberOfHeavyContainers=5, maxNumberOfRefrigeratedContainers=2,
                             maxNumberOfLiquidContainers=3, fuelConsumptionPerKM=1)
        return Ship(ship_id=uuid4(), port=port, configs=configs)


class MediumShipBuilder(ShipBuilder):
    def build_ship(self, port) -> Ship:
        configs = ConfigShip(total_weight_capacity=100000, max_number_of_all_containers=50,
                             maxNumberOfHeavyContainers=10, maxNumberOfRefrigeratedContainers=5,
                             maxNumberOfLiquidContainers=7, fuelConsumptionPerKM=2)
        return Ship(ship_id=uuid4(), port=port, configs=configs)


class HeavyShipBuilder(ShipBuilder):
    def build_ship(self, port) -> Ship:
        configs = ConfigShip(total_weight_capacity=200000, max_number_of_all_containers=100,
                             maxNumberOfHeavyContainers=20, maxNumberOfRefrigeratedContainers=10,
                             maxNumberOfLiquidContainers=15, fuelConsumptionPerKM=3)
        return Ship(ship_id=uuid4(), port=port, configs=configs)
