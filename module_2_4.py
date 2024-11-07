numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print('Входной список : ', '\n', numbers, '\n', 'количество элементов :', len(numbers), )
primes = []  # список простых чисел
not_primes = []  # список  не простых чисел
count = len(numbers)  # количество элементов
print('\r  ') # сброс строк
i=0
while i < len(numbers):
    if int(numbers[i]) <= 1:  # число 1 не является ни простым, ни составным
            i += 1

    num = int(numbers[i])

    v_= int(num ** 0.5)
    is_prime = True
    for j in range(2, int(num ** 0.5)+1 ):       # проверка до sqrt(num)
        if num % j == 0:
            is_prime = False
            break
    if is_prime == True:
            primes.append(numbers[i])           # список простых чисел
    else:
            not_primes.append(numbers[i])       # список составных чисел
    i += 1
    continue
print('Проверка простых чисел закончена','\r')
print('primes :',primes,'\r')
print('not_primes :',not_primes)