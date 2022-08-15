salary = {}
try:
    with open('salary.txt', 'r', encoding="utf-8") as my_file:
        for line in my_file:
            salary[line.split()[0]] = float(line.split()[1])
        print('Зарплата меньше 20.000: ')
        for name, wage in salary.items():
            if wage < 20000:
                print(name)
        print(f'средняя зарплата {round(sum(salary.values()) / len(salary), 2)}')
except IOError:
    print('Нет данных')
