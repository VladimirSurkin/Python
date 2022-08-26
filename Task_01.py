# Task_01

# from datetime import data

class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def get_class(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"@classmethod:\nДата - {data},\nДень - {day}, {type(day)}\nМесяц - {month}, {type(month)}, \nГод - {year}, {type(year)}"
        except ValueError:
            return '@classmethod: Указана неправильная дата!'

    @staticmethod
    def get_static(data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            if 1 <= day <= 31:
                if 1 <= month <= 12:
                    if 2022 >= year >= 1000:
                        return f"@staticmethod:\nВы указали дату: {data}"
                    else:
                        return f"@staticmethod:\nНеправильно указали год ({data}), укажите в формате (гггг)"
                else:
                    return f"@staticmethod:\nНеправильно указали месяц ({data}), укажите в формате (мм) от 01 до 12"
            else:
                return f"@staticmethod:\nНеправильно указали день ({data}), укажите в формате (дд) от 1 до 31"

        except ValueError:
            return '@staticmethod: Указана неправильная дата!'

data = input("Введите дату в формате - дд-мм-гггг: ")
print(Data.get_static(data))
print(Data.get_class(data))

