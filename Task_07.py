# Task_07

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if (self.b + other.b) > 0:
            return f'Сумма комплексных чисел = {self.a + other.a} + {self.b + other.b} * i'
        else:
            return f'Сумма комплексных чисел = {self.a + other.a} {self.b + other.b} * i'

    def __mul__(self, other):
        if (self.a * other.b + (self.b * other.a)) > 0:
            return f'Произведение комплексных чисел = {(self.a * other.a - (self.b * other.b))} + {(self.a * other.b + (self.b * other.a))} * i'
        else:
            return f'Произведение комплексных чисел = {(self.a * other.a - (self.b * other.b))} {(self.a * other.b + (self.b * other.a))} * i'


c_1 = ComplexNumber(2, -7)
c_2 = ComplexNumber(3, 8)
print(c_1 + c_2)
print(c_1 * c_2)
