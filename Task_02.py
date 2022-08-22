# Task_02
from abc import ABC, abstractmethod


class My_clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        My_clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        total_res = My_clothes.result
        My_clothes.result = 0
        return f"{total_res}"


class Coat(My_clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(My_clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)


coat = Coat(44)
costume = Costume(170)
print(coat + costume)
