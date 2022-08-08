# 1.
def func_del(n_1, n_2):
    try:
        result = n_1 / n_2
        print("Ответ n_1 / n_2: ", result)
    except ZeroDivisionError:
        print("Error")


func_del(int(input('Введите число n_1: ')), int(input('Введите число n_2: ')))
