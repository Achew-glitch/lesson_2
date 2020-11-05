my_string = input('Введите строку: ')

my_string = my_string.split(" ")

print(my_string)

for ind, el in enumerate(my_string):
        print(ind + 1, el[0:10])
