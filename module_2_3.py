my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # исходные список
print('Исходные данные :',my_list,'всего',len(my_list),'элементов')
my_positiv_list = []                                    # список положительных
i = 0
while i < len(my_list):
    if my_list[i] == 0:
        i+=1
        continue
    if my_list[i] > 0:
                my_positiv_list.append(my_list[i])
                i+=1
                continue
    print('Выбранные положительные числа : ',my_positiv_list,'всего',len(my_positiv_list),'элементов')
    break              # окончание цикла