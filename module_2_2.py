def number_line():  # функция ввода числа и проверяем что не строка букв
    global count
    while True:
        count = 0
        count = input("Введите значение: ")     # числа или буквы
        if count.isdigit() == True:
            break
        else:
            print('ошибка - введены буквы')
        continue

while True:
    quest=input('''Сравнить числа "Да"-ввести 1, "Нет"-ввести 0 ?''')  # вопрос

    if quest=='1':
        print('Начать сравнение')           # процедура сравнения

        number_line()                       # вводим количество чисел для сравнения
        number = int(count)
        print('вводим числа для сравнения: ')
        digit = []  # список чисел
        i = 0
        while i < number:
            number_line()                    # вводим числа для сравнения
            digit.insert(i, count)
            i += 1
            continue
        print('полученные числа для сравнения :', digit)
        digit_s=set(digit)                  # копируем список в множество чисел для сравнения
# print('числа для сравнения: ',digit_s )
        number_s=len(digit_s)                # количество чисел для сравнения в множестве

        if number == number_s:
            print('числа', digit, 'равных нет, результат:', 0)
        elif number_s == 1:
            print('числа', digit, 'все равны, результат:', 3)
        elif number-number_s >= 1:
            print('числа', digit, ' не все равны, результат:', 2)
    else:
        print('Сравнение не требуется')
        break

    continue