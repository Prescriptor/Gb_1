class ValueError(Exception):
    @staticmethod
    def __init__(error):
        print(error)

class Data:

    @classmethod
    def get_number(cls, number):
        result = list(map(int, number.split("-")))
        return result

    @staticmethod
    def val_number(number):
        date = int(Data.get_number(number)[0])
        month = int(Data.get_number(number)[1])
        year = int(Data.get_number(number)[2])
        long_month = [1, 3, 5, 7, 8, 10, 12]
        shot_month = [4, 6, 9, 11]
        feb_month = [2]
        result = []
        if month in shot_month and 0 < date <= 30 or month in long_month and 0 < date <= 31:
            result.append(date)
        elif month in feb_month and 0 < date <= 28 or month in feb_month and 0 < date <= 29 and year % 4 == 0:
            result.append(date)
        # else:
        #     ValueError('Date error')
        if 0 < month <= 12:
            result.append(month)
        # else:
        #     ValueError('month error')
        if 1972 < year <= 2033:
            result.append(year)
        # else:
        #     ValueError('year error')
        if len(result) == 3:
            return result
        else:
            ValueError('Value error')


print(Data.get_number('12-11-2020'))
print(Data.val_number('30-11-2020'))
