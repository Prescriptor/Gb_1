class ZeroDivError(Exception):
    def __init__(self):
        print('недопустимое число')


while True:
    x = int(input('Введите число: '))
    try:
        1 / x
    except ZeroDivisionError:
        ZeroDivError()
    else:
        print('Всё оk')
