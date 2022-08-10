# 5
from functools import reduce

list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100..1000]: ", list)
print("Произведение всех элементов списка: ", reduce(lambda x, y: x * y, list))
