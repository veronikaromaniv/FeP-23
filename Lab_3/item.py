from abc import ABC, abstractmethod
from uuid import uuid4


class Item(ABC):
    def __init__(self, ID, weight):
        self.ID = ID
        self.weight = weight
        self.count = 0
        self.containerID = uuid4()

    @abstractmethod
    def consumption(self):
        pass

    def getTotalWeight(self):
        return self.weight * self.count


class Small(Item):
    def consumption(self):
        return self.weight * 1.5


class Heavy(Item):
    def consumption(self):
        return self.weight * 2.0


class Refrigerated(Item):
    def consumption(self):
        return self.weight * 3.0


class Liquid(Item):
    def consumption(self):
        return self.weight * 2.5
