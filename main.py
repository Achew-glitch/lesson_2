string = 'abrakadabra'
str_reverse = ''
symbols = list(string)
for el in range(len(string) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(string) - el - 1]
    symbols[len(string) - el - 1] = tmp
str_reverse = ''.join(symbols)
print(str_reverse)

print('Symple sTring'.isupper())

print('cRystaLL'.capitalize())

my_set = {None, 400, 'test', True}

my_set.discard(400)
print(my_set)

is_checked = False
mode = 'checked' if is_checked else 'not checked'
print(mode)

my_list = [10, 20, 20, 20, 30, 40, 50, 60, 30]
print(set(my_list))
print(max(set(my_list), key = my_list.count))