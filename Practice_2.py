my_list = []
length = int(input('Какой длинны будет список: '))

print('Заполните список: ')

for i in range(length):
    my_list.append(input())

print(f'Вы заполнили список: {my_list}')
if len(my_list) % 2 == 0:
    for el in range(0,len(my_list), 2):
        my_list.insert(el, my_list.pop(el+1))
else:
    for el in range(0,len(my_list)-1, 2):
        my_list.insert(el, my_list.pop(el+1))

print(my_list)