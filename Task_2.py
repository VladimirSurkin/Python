#2

my_list = input("Введите элементы списка: ")
i = input("Укажите разделитель в списке: ")

my_list = my_list.split(i)
for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)