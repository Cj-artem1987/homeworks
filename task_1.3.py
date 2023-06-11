from random import *

days_in_month = [
    ['Январь', 31],
    ['Февраль', [28, 29]],
    ['Март', 31],
    ['Апрель', 30],
    ['Май', 31],
    ['Июнь', 30],
    ['Июль', 31],
    ['Август', 31],
    ['Сентябрь', 30],
    ['Октябрь', 31],
    [' Ноябрь', 30],
    ['Декабрь', 31], ]
x = int(input('Введите номер месяца: '))
x -= 1
if 0 <= x <= 11:
    if days_in_month[x][1] == 31:
        print(f'Вы ввели {days_in_month[x][0]}. {days_in_month[x][1]} день.')
    elif x == 1:
        print(f'Вы ввели {days_in_month[x][0]}. {days_in_month[x][1][0]} или {days_in_month[x][1][1]} дней')
    else:
        print(f'Вы ввели {days_in_month[x][0]}. {days_in_month[x][1]} дней.')

else:
    print('Такого месяца нет!')