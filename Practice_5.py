rating_list = [5, 4, 3, 2, 2, 1]
tmp = None
print(f'Текущий рейтинг: {rating_list}')

while True:
    new_el = input('Введите число: ')

    if new_el == 'exit':
        break

    new_el = int(new_el)

    if tmp:
        rating_list.remove(tmp)
        tmp = None

    for el in rating_list:
        if new_el > el:
            rating_list.insert(rating_list.index(el), new_el)
            tmp = new_el
            break
    else:
        rating_list.append(new_el)
        tmp = new_el

    print(f'Новый рейтинг: {rating_list}')
