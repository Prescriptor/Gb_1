store_availabal = []
equipment_availabal = []
office_availabal = []
i = 0


def main_menu():
    print('Добро пожаловать в программу "Склад"')
    while True:
        data = input('Что бы оприходовать материалы введите "Приход" \n'
                     'Что бы проверить остаток материалов на складе введите "Остаток" \n'
                     'Для выхода - наберите "Выход": ')
        if data.lower() == 'приход':
            Equipment.obtaining()
        if data.lower() == 'остаток':
            print(f'Остаток на складе: {Store.get_availability()}')
            print(f'Наличие в офисе: {Office.get_availability()}')
        if data.lower() == 'выход':
            break


class Store:
    """Класс, описывающий склад"""

    def __init__(self):
        # self.location = location
        pass

    @staticmethod
    def get_availability():  # Метод присвоения оборудования подразделению "Офис"
        store_availabal = []
        for el in equipment_availabal:
            if el.get('location') == 'store':
                store_availabal.append(el)
            elif el.get('location').lower() == 'склад':
                el.update(location='store')
                store_availabal.append(el)
            elif el.get('location') == None:
                el.update(location='store')
                store_availabal.append(el)
        return store_availabal


class Office(Store):
    """Класс, описывающий выданное оборудование"""

    @staticmethod
    def get_availability():  # Метод присвоения оборудования подразделению "Офис"
        office_availabal = []
        for el in equipment_availabal:
            if el.get('location') == 'office':
                office_availabal.append(el)
            elif el.get('location').lower() == 'офис':
                el.update(location='office')
                office_availabal.append(el)
        return office_availabal

    def to_give(self, t_type, brand, quantity, serial_number, location):
        pass


class Equipment:
    """Класс «Оргтехника»"""

    def __init__(self, t_type, brand, quantity, location=None):
        self.t_type = t_type
        self.brand = brand
        self.quantity = quantity
        self.location = location

    def get_equipment(self):
        equipment_availabal.append(self.__dict__)
        return equipment_availabal

    def equipment_location(self, quant, location):  # функция смены подразделения приписки.
        self.location = location
        # copy_dict = dict(self.__dict__)
        # copy_dict.update(dict(quantity=quant))
        # print(f'dfvdfvfvdv ------------- {str(copy_dict.values())}')
        # some = Equipment(copy_dict.values())
        # some.get_equipment()
        # self.__dict__.update(dict(quantity=self.__dict__.get("quantity") - quant))
        # # print(f'{self.__dict__} - ЗДЕСЬ!!!!!!!!!!!!!!!')
        self.__dict__.update(dict(location=self.location))
        return self.__dict__

    @staticmethod
    def obtaining():
        t_type = input('Введите тип устройства: ')
        brand = input('Введите производителя: ')
        while True:
            try:
                quantity = input('Введите количество устройств: ')
                if int(quantity) > 0:
                    break
            except ValueError:
                print('Введите целое число больше нуля!')
        location = input('Введите местоположение устройства: ')
        some = Equipment(t_type, brand, quantity, location)
        some.get_equipment()


# class Printer(Equipment):
#     def __init__(self, t_type, brand, quantity, serial_number, is_color):
#         super().__init__(t_type, mark, quantity, serial_number)
#         self.is_color = is_color
#         # self.
#
# class Scanner(Equipment):
#     def __init__(self, t_type, brand, quantity, serial_number, format):
#         super().__init__(t_type, brand, quantity, serial_number)
#         self.format = format
#         # self.
#
# class Xerox(Equipment):
#     def __init__(self, t_type, brand, quantity, serial_number, speed):
#         super().__init__(t_type, brand, quantity, serial_number)
#         self.speed = speed
#         # self.

# priner_1 = Equipment("priner", "HP", 1, "store")
# priner_1.get_equipment()
# priner_2 = Equipment("priner", "Samsung", 2, None)
# priner_2.get_equipment()
# priner_3 = Equipment("priner", "Lexmark", 3)
# priner_3.get_equipment()
# print(f'Доступное оборудование: {equipment_availabal}')
# print(f'Инвентаризация склада: {Store.get_availability()}')
#
# print('Меняем локацию первого принтера')
# priner_1.equipment_location(1, 'office')
# print(f'Остаток на складе: {Store.get_availability()}')
# print(f'Наличие в офисе: {Office.get_availability()}')

main_menu()
