'''
Реализуйте базовый класс Airplane. 
У данного класса должны быть следующие атрибуты: speed, color, name, is_jet (булево).  
А также методы: go, stop, direction, которые должны сообщать, что самолет летит, не летит, повернул в полете. 
Опишите несколько дочерних классов самолетов: FastAirplane, Biplane, ArmyAirplane. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость самолета. 
Для класса FastAirplane переопределите метод show_speed. 
При значении скорости свыше 1300 (FastAirplane) должно выводиться сообщение о сверхзвуковой скорости. 
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
'''


class Airplane:

    def __init__(self, speed, color, name, is_jet):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_jet = is_jet

    def go(self):
        print(f"{self.name} летит")

    def stop(self):
        print(f"{self.name} остановился")

    def direction(self, dir):
        print(f"{self.name} повернул на {dir}")

    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed} км/ч")


class FastAirplane(Airplane):

    def show_speed(self):
        if self.speed > 1300:
            print(
                f"Скорость {self.name} превышает 1300 км/ч - самолёт вышел на сверхзвуковую скорость"
            )
        else:
            super().show_speed()


class Biplane(Airplane):
    pass


class ArmyAirplane(Airplane):
    pass


fast_plane = FastAirplane(1400, "серебристый", "Сверхзвуковой", True)
fast_plane.show_speed()
fast_plane.go()
fast_plane.direction("юго-восток")
fast_plane.stop()

print('\n' + '=' * 20 + '\n')

biplane = Biplane(200, "синий", "Биплан", False)
biplane.show_speed()
biplane.go()
biplane.direction("северо-запад")
biplane.stop()

print('\n' + '=' * 20 + '\n')

army_plane = ArmyAirplane(800, "зеленый", "Военный", True)
army_plane.show_speed()
army_plane.go()
army_plane.direction("восток")
army_plane.stop()
