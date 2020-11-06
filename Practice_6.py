goods = []
ind = 0
params = {}

while True:
    params.update({'название' : input('название товара: '),
                       'цена' : input('цена товара: '),
                       'количество' : input('количество товара: '),
                       'единица измерения' : input('единица измерения товара: ')})
    ind += 1
    goods.append((ind, params.copy()))

    print(goods)

    next_step = input('Добавить еще товар?\n')
    if next_step == 'no' or next_step == 'нет':
        break

params = list(zip(*goods))[1]

name_list = []
price_list = []
count_list = []
unit_list = []

for el in params:
    name_list.append(el.get('название'))
    price_list.append(el.get('цена'))
    count_list.append(el.get('количество'))
    unit_list.append(el.get('единица измерения'))

a_goods = {'название': name_list, 'цена': price_list, 'количество': count_list, 'единица_измерения': unit_list}

print(a_goods)

