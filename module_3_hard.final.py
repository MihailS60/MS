def split_sructure_list(_str, len_list):
    for i in range(len(_str)):
        if isinstance(_str[i], str) == True:  # проверка на наличие строки в списке
            _str[i] = len(_str[i])
        if len_list == 0:
            return 0
    else:
        return int(_str[len_list - 1]) + int(split_sructure_list(_str, len_list - 1))

def split_sructure_dict(data_d):
    result_unpack = []
    result_dict = []
    items = list(data_d.items())  # перевод в список
    result_unpack = unpack_(items)  # распаковка структуры
    result_dict = split_sructure_list(result_unpack, len(result_unpack))

    return result_dict

def split_sructure_tuple(data_s):
    sum_ = 0
    for item in data_s:
        if isinstance(item, int) == True:  # проверка на целое
            sum_ += int(item)
        elif isinstance(item, str) == True:  # проверка на строку
            sum_ += len(item)
        elif isinstance(item, list) == True:  # проверка на список
            sum_ += split_sructure_tuple(item)
        elif isinstance(item, tuple) == True:
            if item == ():
                sum_ += 0
            else:
                sum_ += split_sructure_tuple(item)
        elif isinstance(item, dict) == True:    # проверка на словарь
            sum_ += split_sructure_dict(item)
        elif isinstance(item, set) == True:     # проверка на множество
            sum_ += split_sructure_tuple(item)
        continue

    return sum_

def unpack_(list_structure):  # распаковка вложенной
    flat_list = []
    for sublist in list_structure:
        for item in sublist:
            flat_list.append(item)

    return flat_list





data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print('заданная строка ', data_structure)
data_structure_lenth = len(data_structure)
print('количество вложенных элементов : ', data_structure_lenth)

print('Структура списка :')
print(data_structure[0])
print(data_structure[1])
print(data_structure[2])
print(data_structure[3])
print(data_structure[4])
print('_' * 20)

sum_ = 0

for item in data_structure:

    if isinstance(item, int) == True:  # проверка на целое
        sum_ += int(item)
    elif isinstance(item, str) == True:  # проверка на строку
        sum_ += len(item)
    elif isinstance(item, list) == True:  # проверка на список
        sum_ += split_sructure_list(item, int(len(item)))
    elif isinstance(item, tuple) == True:   # проверка на кортеж
        sum_ += split_sructure_tuple(item)
    elif isinstance(item, dict) == True:    # проверка на словарь
        sum_ += split_sructure_dict(item)
    continue

print('Итоговая сумма :',sum_ )