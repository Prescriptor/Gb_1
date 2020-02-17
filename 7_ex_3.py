class Kletka:
    def __init__(self, cell_pcs, each=5):
        self.cell_pcs = cell_pcs
        self.each = each

    def make_order(self):
        m = len(self.obg) // self.each
        o = len(self.obg) % self.each
        block = ('* ' * self.each + '\n') * m + '* ' * o
        return block

    def __str__(self, data):
        self.data = ('*' * data)
        return self.make_order()

    def __add__(self, other):
        summ = self.cell_pcs + other.cell_pcs
        return self.__str__(summ)

    def __sub__(self, other):
        a = self.cell_pcs
        b = other.cell_pcs
        if a > b:
            sub = a - b
        else:
            sub = b - a
        return self.__str__(sub)

    def __mul__(self, other):
        multy = self.cell_pcs * other.cell_pcs
        return self.__str__(multy)

    def __truediv__(self, other):
        a = self.cell_pcs
        b = other.cell_pcs
        if a > b:
            sub = a // b
            return self.__str__(sub)
        else:
            return 'Деление не возможно'


a = Kletka(5, 4)
b = Kletka(2, 4)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
