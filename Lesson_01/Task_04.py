# 4
number = int(input('Введите целое положительное число: '))

while number < 0:
    print('Вы ввели отрицательное число.')
    number = int(input('Введите целое положительное число: '))

i = number
n = number
a = 0

while i != 0:
    i = n // 10
    n = n % 10
    if a > n:
        a = a
    else:
        a = n
    if i > 10:
        n = int(i)
    else:
        n = int(i)
        if a > n:
            a = a
        else:
            a = n
        print('Самое большая цифра -', a, 'в числе', number)
        break
