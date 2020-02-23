result = []


class TypeOfData():
    def __init__(self, el):
        self.el = el
        if self.el == 'stop':
            exit(0)
        else:
            print(f'недопустимое значение {el}')


class Exception:
    @staticmethod
    def except_func():
        while True:
            x = input('Введите данные: ')
            interim = list(x.split(' '))
            for el in interim:
                try:
                    result.append(int(el))
                except ValueError:
                    TypeOfData(el)
            print(result)


Exception.except_func()

