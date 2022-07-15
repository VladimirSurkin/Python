# 2

seconds_in_hour = 3600
seconds_in_minute = 60

seconds = int(input("Введите время в секундах (от 0 до 86399): "))

while (seconds < 0 or seconds > 86399):
    print('Вы указали некорректное время в секундах.')
    seconds = int(input('Введите время в секундах (от 0 до 86399): '))

hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print(" {0:.0f} : {1:.0f} : {2:.0f}".format( hours, minutes, seconds))