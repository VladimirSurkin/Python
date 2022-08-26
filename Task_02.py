class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def f_null():
    try:
        num_1 = int(input('Введите число n_1: '))
        num_2 = int(input('Введите число n_2: '))
        if num_2 == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = num_1 / num_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print("Результат деления числа n_1 на n_2 равен:", f_null())
