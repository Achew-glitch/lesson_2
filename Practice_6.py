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

a_goods = {key: [] for key in params[0].keys()}

for el in params:
    for key, value in el.items():
        a_goods[key].append(value)

print(a_goods)