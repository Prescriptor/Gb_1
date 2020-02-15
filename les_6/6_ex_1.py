from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self, color, time):
        self.__color = (('красный', 7), ('желтый', 2), (color, time))

    def running(self):
        for color, time in cycle(self.__color):
            print(color)
            sleep(time)


semaphor = TrafficLight('zeleniy', 3)
semaphor.running()
