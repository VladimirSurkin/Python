class Stationery:
    title = "\n<< Канцелярская принадлежность >>"

    def draw(self):
        print("Запуск отрисовки (метод класса Stationery)")


class Pen(Stationery):
    def draw(self):
        print("1. Рисунок ручкой (метод класса Pen)")


class Pencil(Stationery):
    def draw(self):
        print("2. Зарисовка карандашом (метод класса Pencil)")


class Highlighter(Stationery):
    def draw(self):
        print("3. Выделение маркером (метод класса Highlighter)")


s = Stationery()
print(s.title)
s.draw()

p_1 = Pen()
p_1.draw()

p_2 = Pencil()
p_2.draw()

h = Highlighter()
h.draw()
