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
