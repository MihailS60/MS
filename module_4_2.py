from random import randint

def test_function(b1,b2):
    num = randint(b1, b2)

    def inner_function():
            print('Я в области видимости функции test_function печатаю num ',num)

    inner_function()
    return


test_function(1,10)

inner_function()                    # функция невидима вне области видимости test_function(b1,b2)