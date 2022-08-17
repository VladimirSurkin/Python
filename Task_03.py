# Task_03
class Worker:
    name = "Соколов"
    surname = "Илья"
    position = "Экономист"
    wage = 50000
    bonus = 20000
    _income = {"Оклад": wage, "Премия": bonus}


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.surname)

    def get_full_income(self):
        self.total_income = self.wage + self.bonus
        return ", доход с учётом премии: {}".format(self.total_income)


print(Position().get_full_name() + str(Position().get_full_income()) + " " + str(Worker()._income))
