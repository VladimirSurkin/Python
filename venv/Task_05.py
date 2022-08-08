def cal():
    total_sum = 0
    while True:
        numbers = input('Введите числа через пробел. Для выхода укажите "*": ').split(' ')
        try:
            if numbers == "*":
                break
            else:
                total_sum += sum(map(int, numbers))
                print(total_sum)
        except ValueError:
            break


cal()
