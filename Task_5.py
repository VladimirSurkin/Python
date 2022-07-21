#5

my_list = [7, 5, 3, 3, 2]
result = my_list.copy()

number = int(input("Введите натуральное число: "))
while number <= 0:
    print("Вы ввели некоректные данные.")
    number = int(input("Введите натуральное число: "))

# n_max=int(max(result))
# n_min=int(min(result))

# if number in result:
#     n = result.index(number)
#     result.insert(n, number)
# else:
# if number < n_min:
#     result.insert(result.index(min(result)) + 1, number)
# elif number > n_max:
#     result.insert(result.index(max(result)), number)
# else:
#     for i,v in enumerate(result):
#         if number<v:
#             i+=i
#         else:
#             result.insert(i, number)
#             break

if number < int(min(result)):
    result.insert(result.index(min(result)) + 1, number)
else:
    for i, v in enumerate(result):
        if number < v:
            i += i
        elif number == v:
            i += i
        else:
            result.insert(i, number)
            break
print("Набор натуральных чисел: ", my_list)
print("Пользователь ввел число ", number, ". Результат: ", result)
