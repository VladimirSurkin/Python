# Task_03

class NumError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def num_check(self):

        global num
        while True:
            try:
                try:
                    print('Для остановки программы укажите в строке - stop')
                    num = input('Введите число: ')
                    if num == 'stop':
                        print("Программа остановлена.\nСписок введенных чисел:", self.my_list)
                        break
                    else:
                        num = float(num)
                        if type(num) == float:
                            self.my_list.append(num)
                        else:
                            raise NumError
                except ValueError:
                    raise NumError
            except NumError:
                print("Вы ввели не число. Для остановки программы укажите в строке - stop")


a = TypeCheck()
a.num_check()
