class Matrix:
    def __init__(self, listing):
        self.listing = listing

    def __str__(self, massive=None):  # Приводит массив массивов к традиционному виду
        if massive == None:
            massive = self.listing # Принимает первоначальный массив массивов, если суммирование не производилось
        fin_listing = ''
        step = 0
        while step < len(self.listing[0]):
            fin_listing += str(massive[step]) + '\n'
            step += 1
        return (fin_listing)

    def stapler(self, mtrx_result):  # создаёт массив массивов
        massive = []
        start, stop, step = 0, 0, len(self.listing)
        while stop < len(mtrx_result):
            start = stop
            stop += step
            massive.append(list(mtrx_result[start:stop]))
        return self.__str__(massive)

    def cutter(self, listings, el):  # Возвращает один массив из массива массивов.
        block = (listings[el])
        return block

    def __add__(self, other): # поэлементно складывает массивы массивов
        mtrx_result = []
        i = 0
        while i < len(self.listing): # Пока массив массивов не исчерпан:
            mtrx1 = self.cutter(self.listing, i)  # По-одному возвращает массивы из массива массивов
            mtrx2 = other.cutter(other.listing, i)  # По-одному возвращает массивы из массива массивов
            mtrx_result += (list(map(lambda a, b: a + b, mtrx1, mtrx2)))  # Складывает фрагменты массивов
            i += 1
        return self.stapler(mtrx_result) # Отправляет массив на формирование массива массивов (для удобного представления в традиционном виде)


mtrx1 = Matrix([[2, 1, 3], [4, 6, 5], [8, 7, 9]])
mtrx2 = Matrix([[3, 2, 1], [6, 5, 4, ], [9, 8, 7]])
print(mtrx1)
print(mtrx2)
print(mtrx1.__add__(mtrx2))
