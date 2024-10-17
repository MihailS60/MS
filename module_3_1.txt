def counter():
    calls = 0
    def count_calls():
        nonlocal calls
        calls +=1
        print('счетчик обращений : ',calls)
        return calls
    return count_calls

def string_info(string):
    global data
    data=(len(string),string.upper(),string.lower())
    number_calls()
    return data

def is_contains(string,list_to_search):
    global compare          # результат поиска
    elem = ''               # преобразование списка в строку
    for el_ in list_to_search:
        elem += el_
    s_l = string.lower()  # Регистром строки при проверке пренебречь
    s_e = elem.lower()  # Регистром строки при проверке пренебречь

    if (s_e.find(s_l)) !=-1:        # номер первого вхождения
        compare=True                # присутствует
    else:
        compare=False               # отсутствует
    number_calls()
    return


number_calls = counter()   # создаем счетчик
print('_________________________________')
string ='Capybara'
data=string_info(string)
print(data)
print('_________________________________')
string ='Armageddon'
data=string_info(string)
print(data)
print('_________________________________')
string ='Urban'
print('поисковая подстрока : ',string)
list_to_search=['ban', 'BaNaN', 'urBAN']
print('список для поиска: ',list_to_search)

is_contains(string,list_to_search)
print('результат поиска : ',compare)

print('_________________________________')
string ='Urban1'
print('поисковая подстрока : ',string)
list_to_search=['ban', 'BaNaN', 'urBAN']
print('список для поиска: ',list_to_search)

is_contains(string,list_to_search)
print('результат поиска : ',compare)

print('_________________________________')
string ='cycle'
print('поисковая подстрока : ',string)
list_to_search=['recycling', 'cyclic']
print('список для поиска: ',list_to_search)

is_contains(string,list_to_search)
print('результат поиска : ',compare)