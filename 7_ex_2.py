from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return f'Общий расход ткани: {Coat(self.size).calc + Costume(other.size).calc}'

class Coat(Clothes):
    @property
    def calc(self):
        size = self.size / 6.5 + 0.5
        return size


class Costume(Clothes):
    @property
    def calc(self):
        size = self.size * 2 + 0.3
        return size


coat = Coat(48)
print(coat.calc)
costume = Costume(1.7)
print(costume.calc)
print(coat + costume)