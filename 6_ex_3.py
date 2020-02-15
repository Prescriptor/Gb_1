# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = ' '.join([self.name, self.surname])
        return f'ФИО: {full_name}'

    def get_total_income(self):
        summ = self._Worker__income.get('wage') + self._Worker__income.get('bonus')
        return f'Общий доход: {summ}'


worker1 = Position('Генадий', 'Серов', 'Сотрудник отдела кадров', 20000, 5000)
worker2 = Position('Федор', 'Сумкин', 'Сотрудник логистичесого отдела', 10000, 1)

print(worker1.get_full_name())
print(worker1.get_total_income())
print(worker2.get_full_name())
print(worker2.get_total_income())
