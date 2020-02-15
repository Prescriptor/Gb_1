# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil(карандаш), Handle(маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Начало отрисовки Pen')


class Pencil(Stationery):
    def draw(self):
        print('Старт прорисовки Pencil')


class Handle(Stationery):
    def draw(self):
        print('Запуск зарисовки Handle')


scribbler = Pen('scribbler')
stick = Pencil('stick')
marker = Handle('marker')

scribbler.draw()
stick.draw()
marker.draw()
