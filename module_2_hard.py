import random                          # генератор случайных чисел
def get_number():
    num = 0
    number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num = random.choice(number)
    return num

num = get_number()
print('Получено случайное число :', num)
print('__________________________')

pass_ = []
for i in range(1, (num // 2 + 1)):  # число сочетаний из 2 по n (первая половина)
    if i == (num / 2):              # ОКОНЧАНИЕ ЦИКЛА ДЛЯ ЧЕТНЫХ ЧИСЕЛ
        break
    pass_.append([])
    for j in range(i + 1, num):
        if (i + j) > num:           # окончание цикла если "пара чисел" больше num
            break
        if num % (i + j) == 0:
            pass_[i - 1].append(i)
            pass_[i - 1].append(j)
    continue

print('Список выбранных пар для числа ', num, '\n', pass_)
pass_list = ''                      # перевод  списка в строку
for i in range(0, len(pass_)):
    pass_list = pass_list + (' '.join(map(str, (pass_[i]))))
print('__________________________')
print(f"Пароль для числа {num} : ",pass_list)