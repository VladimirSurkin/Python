# 3.
def my_func(n_1, n_2, n_3):
    a = n_1 + n_2 + n_3 - min(n_1, n_2, n_3)
    print(a)


my_func(int(input('Введите число n_1: ')), int(input('Введите число n_2: ')), int(input('Введите число n_3: ')))
