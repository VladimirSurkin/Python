# 5
revenue = int(input('Укажите выручку в тыс. руб.: '))
cost = int(input('Укажите издержки в тыс. руб.: '))
financial_result = revenue - cost

if financial_result > 0:
    print('Ваша фирма работает с прибылью. Прибыль составила -', financial_result, 'тыс. руб.')
    print('Рентабильность выручки составила -', (financial_result / revenue) * 100, '%')
    number_employees = int(input('Укажите численность сотрудников фирмы:'))
    print('Прибыль на одного сотрудника  составила -', financial_result / number_employees, 'тыс. руб.')
else:
    print('Убыток составил -', financial_result, 'тыс. руб.')
