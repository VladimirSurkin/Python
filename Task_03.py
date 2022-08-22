# Task_03
from abc import ABC, abstractmethod


class Cell:
    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return f'Сумма клеток: {self.count + other.count}'

    def __sub__(self, other):
        result = self.count - other.count
        return f'Разность клеток: {result}' if result > 0 else 'Остаток не может быть посчитан, результат меньше нуля'

    def __mul__(self, other):
        return f'Результат умножения клеток составляет: {self.count * other.count}'

    def __truediv__(self, other):
        return f'Результат деления клеток составляет: {self.count // other.count}'

    def make_order(self, rows):
        result = ''
        for i in range(int(self.count / rows)):
            result += '*' * rows + '\n'
        result += '*' * (self.count % rows) + '\n'
        return result


cell = Cell(12)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(5))
