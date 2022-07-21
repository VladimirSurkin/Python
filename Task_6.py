#6
result_dict = {}
while True:
    t="-"
    p=' '
    print(t*50)
    print('Реализация структуры данных «Товары»')
    print(t*50)
    print(p*20,'Меню')
    print(t*50)
    print('Ввести новый список товаров (n)')
    print('Посмотреть аналитику (a)')
    print('Выйти из меню (q)')
    print(t*50)
    q_1=input(':')

    if q_1 == 'q':
        print('')
        break
    elif q_1=='a':
        if result_dict == {}:
            print ('Данных для анализа нет. Пожалуйста, внесите новый список товаров.')
            q_1 = input('Вернуться в меню (да/нет)? ')
            if q_1 == 'да' or q_1 == 'yes' or q_1 == 'y' or q_1 == 'д':
                q_1 = 'yes'
            else:
                q_1 = 'no'
                break
        else:
            print('-' * 100)
            print(result_dict)
            print('-' * 100)
            q_1 = input('Вернуться в меню (да/нет)? ')
            if q_1 == 'да' or q_1 == 'yes' or q_1 == 'y' or q_1 == 'д':
                q_1 = 'yes'
            else:
                q_1 = 'no'
                break
    elif q_1=='n':
        goods = []
        result_list = []
        q_1 = 'yes'
        i = 1
        while q_1 == 'да' or q_1 == 'yes' or q_1 == 'y' or q_1 == 'д':
            print('Товар №:', i)
            q_2 = input('Наименование товара: ')
            q_3 = int(input('Стоимость товара: '))
            q_4 = int(input('Количество товара: '))
            q_5 = input('Единица измерения: ')

            goods.append((i, {'Наименование': q_2, 'Цена': q_3, 'Количество': q_4, 'Ед. изм.': q_5}))

            q_1 = input('Вы хотите внести еще товар (да/нет)? ')

            if q_1 == 'да' or q_1 == 'yes' or q_1 == 'y' or q_1 == 'д':
                q_1 = 'yes'
                i += i
            else:
                break

        result_dict = {}

        for i, val in enumerate(list(goods[0][1].keys())):
            result_dict[val] = []

        for i, val in enumerate(result_dict):
            dict_list = []

            for j, val_goods in enumerate(goods):
                key_val = val_goods[1].get(val)
                if key_val not in dict_list:
                    dict_list.append(key_val)
            result_dict[val] = dict_list

        q_1 = input('Показать аналитику (да/нет)? ')
        if q_1 == 'да' or q_1 == 'yes' or q_1 == 'y' or q_1 == 'д':
            print('-'*100)
            print(result_dict)
            print('-' * 100)
            q_1 = input('Вернуться в меню (да/нет)? ')
            if q_1 == 'да' or q_1 == 'yes' or q_1 == 'y' or q_1 == 'д':
                q_1 = 'yes'
            else:
                break
        else:
            q_1 = input('Вернуться в меню (да/нет)? ')
            if q_1 == 'да' or q_1 == 'yes' or q_1 == 'y' or q_1 == 'д':
                q_1 = 'yes'
            else:
                break
    else:
        print('Вы указали не верную операцию. Повторите попытку.')
