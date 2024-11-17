def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('использование функции print_params с заменой аргументов')
print('вызов функции с аргументами по умолчанию :')
print_params(a = 1, b = 'строка', c = True)  #  вызов функции с аргументами по умолчанию
print('вызов функции без аргументов :')
print_params()
print('вызов функции с разным количеством аргументов :')
print_params('первый аргумент','второй аргумент')
print_params(False)
print_params(c=False)
print_params(b = 25)
print_params(c = [1,2,3])
print('_________________________','\n','все варианты функции с разным количеством аргументов УСПЕШНЫ !')