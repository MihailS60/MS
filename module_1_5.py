# неизменяемая структурa данных(КОРТЕЖ):
immutable_var = (1, 0.5, 3 ,'DATA',True,[1,2,3])
print('ПЕЧАТЬ КОРТЕЖА: ',immutable_var)
print('ПЕЧАТЬ РАЗМЕРА КОРТЕЖА: ',immutable_var.__sizeof__())
# Изменение значений переменных:
# immutable_var[0]=100
# ОШИБКА , нельзя менять!!!
# меняем элементы списка
print(immutable_var[5])
immutable_var[5][1]=100
print(immutable_var[5])
# изменяемая структурa данных:
mutable_list=[1, 0.5, 3 ,'DATA',True,[1,2,3]]
print('СОЗДАН СПИСОК: ',mutable_list)
mutable_list[0] = 200
print('ИЗМЕНЕН СПИСОК: ',mutable_list)
# Перебор элементов
i = 0
while i < len(mutable_list):
    print(mutable_list[i])
    i += 1