# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат

class Car:
    def __init__(self, speed, color, name, is_police, side=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.side = side

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        if self.side == 'right':
            print('Машина повернула вправо')
        elif self.side == 'left':
            print('Машина повернула влево')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('TownCar Скорость превышена!')
        print(f'TownCar Текущая скорость: {self.speed}')


class SportCar(Car):
    print(f'Спортивная')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('WorkCar Скорость превышена!')
        print(f'WorkCar Текущая скорость: {self.speed}')


class PoliceCar(Car):
    print(f'Полицейская')


t_car = TownCar(60, 'baklajan', 'Lada', False, 'right')
p_car = PoliceCar(80, 'gray', 'UAZ', True, 'left')
s_car = SportCar(70, 'yelloy', 'Niva', False, 'left')
w_car = WorkCar(50, 'green', False, 'ZIL')

s_car
p_car
w_car.show_speed()
t_car.show_speed()
t_car.turn()
