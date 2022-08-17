# Task_04
class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСкорость машины {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость машины больше 60 км/ч! Cкорость машины - {self.speed}'
        else:
            return f'Скорость в пределах нормы - {self.name}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость машины больше 40 км/ч! Скорость машины - {self.speed}'
        else:
            return f'Скорость в пределах нормы - {self.name}'


class PoliceCar(Car):
    pass


town = TownCar('Auto_TownCar', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Auto_SportCar', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('Auto_WorkCar', 90, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('налево'), work.stop())

police = PoliceCar('Auto_PoliceCar', 100, 'yellow', True)
print('4:\n' + police.go(), police.show_speed(),
      police.turn('налево за машиной Auto_WorkCar \nДогнала машину Auto_WorkCar и затем'), police.stop())
