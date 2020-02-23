class ComplexNum:
    def __init__(self, nat, img):
        self.nat = nat
        self.img = int(img.split('i')[0])

    def __add__(self, other):
        nat_summ = self.nat + other.nat
        img_sum = self.img + other.img
        return f'{nat_summ} + {img_sum}i'

    def __mul__(self, other):
        mult_num = ((self.nat * other.nat) + (self.img * other.img * -1))
        mult_img = ((self.nat * other.img) + (self.img * other.nat))
        return f'{mult_num} + {mult_img}i'

a = ComplexNum(1, '3i')
b = ComplexNum(2, '1i')
print(a + b)
print(a * b)
