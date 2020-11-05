my_list = [1, 1.2, 'string', True, None, ('touple_1', 'touple_2'), complex(5,6),
           {'set_1', 'set_2'}, {'dict_1' : 'val_1', 'dict_2': 'val_2'}, bytes('text', encoding='UTF-8')]
for el in my_list:
    print(type(el))