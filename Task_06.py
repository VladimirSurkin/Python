from itertools import count, cycle

print("Итератор, генерирующий целые числа, начиная с указанного:")
for item in count(3):
    if item > 10:
        break
    else:
        print(item)

print("Итератор, повторяющий элементы некоторого списка, определенного заранее:")
i = 0
for value in cycle([1, 2, 3, 4]):
    if i > 10:
        break
    print(value)
    i += 1
