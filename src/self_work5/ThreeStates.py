'''
Создать класс ThreeStates и определить у него поле state и метод hasstate. Атрибут state реализовать как приватный. 
В рамках метода реализовать переключение состояний: первое, второе, третье. 
Продолжительность первого состояния составляет 5 секунд, второго — 3 секунды, третьего — 2 секунды. 
Переключение между состояниями должно осуществляться только в указанном порядке (первое, второе, третье). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
import time


class ThreeStates:

    def __init__(self):
        self.__state = 1

    def hasstate(self):
        if self.__state == 1:
            print("Первое состояние (5 секунд)")
            time.sleep(5)
            self.__state = 2
        elif self.__state == 2:
            print("Второе состояние (3 секунды)")
            time.sleep(3)
            self.__state = 3
        elif self.__state == 3:
            print("Третье состояние (2 секунды)")
            time.sleep(2)
            self.__state = 1
        else:
            print("Неизвестное состояние")


ts = ThreeStates()
ts.hasstate()
ts.hasstate()
ts.hasstate()
