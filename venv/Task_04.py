# 4
def my_func(x, y):
    global result_2
    result = x ** y

    result_2 = 1
    for i in range(abs(y)):
        result_2 *= x
    if y < 0:
        result_2 = 1 / result_2
    return result_2
    return result


print("Способ 1 - х в степени у, метод ** ", my_func(int(input('Введите число x: ')), int(input('Введите число y: '))))
print("Способ 2 - х в степени у, метод * ", result_2)
