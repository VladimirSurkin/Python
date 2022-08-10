# 4
list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in list if list.count(i) == 1]

print('Исходный список: ', list)
print('Результат: ', new_list)
