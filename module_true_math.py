import math

def divide(first, second):
    if second==0:
        result = math.inf
    else:
        result = first/second
    return result

print('_'*20)
f_1 = int(input('ввести первое число f_t : ', ))
s_2 = int(input('ввести второе число s_t: ', ))

f_3 = int(input('ввести третье число f_t : ', ))
s_4 = int(input('ввести четвертое число s_t: ', ))
