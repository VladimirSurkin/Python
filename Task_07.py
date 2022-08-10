# 7
from math import factorial


def fact(n):
    for i in range(n + 1):
        print(i, end='! = ')
        yield factorial(i)


n = int(input("Введите число n факториала: "))
for el in fact(n):
    print(el)
