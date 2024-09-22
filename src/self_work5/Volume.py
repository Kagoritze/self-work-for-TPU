'''
Реализовать класс Volume, в котором определить защищенные поля: length (длина), width (ширина) и height (высота). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Определить метод расчета, использовав формулу: длина*ширина*высота. 
Проверить работу метода.
'''


class Volume:

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def calculate_volume(self):
        return self._length * self._width * self._height


v = Volume(5, 3, 2)
print(f"Объем: {v.calculate_volume()}")
