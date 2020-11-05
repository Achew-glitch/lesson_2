month = int(input('Введит номер месяца: '))

dict_month = {(12, 1, 2): 'Зима', (3, 4, 5): 'Весна', (6, 7, 8): 'Лето', (9, 10, 11): 'Осень'}
list_month = ['Зима', 'Весна', 'Лето', 'Осень']

if 0 < month < 13:
    for key in dict_month.keys():
        if month in key:
            print(dict_month.get(key))
else:
    print('Вы используете другую систему счисления')

if 2 < month < 6:
    print(list_month[1])
elif 5 < month < 9:
    print(list_month[2])
elif 8 < month < 12:
    print(list_month[3])
elif 0 < month < 13:
    print(list_month[0])
else:
    print('Вы используете другую систему счисления')