# Task_2
class Road:
    _length = 0
    _width = 0
    _weight = 0
    _depth = 0

    def MyResult(self, _length, _width, _weight, _depth):
        total = _length * _width * _weight * _depth / 1000
        return print(f"Масса асфальта\n {_length} м * {_width} м * {_weight} кг * {_depth} см = ", total, "т")


r = Road()
r.MyResult(20, 5000, 25, 5)
