'''
Реализовать класс MathOperations. 
Определить в нем атрибуты first_num, second_num и метод calc. Метод выводит сообщение “Запуск операции”. 
Создать три дочерних класса my_sum (сложение), my_sub (вычитание), my_mult (умножение). 
В каждом из классов реализовать переопределение метода calc. 
Для каждого из классов метод должен выполнять математическую операцию, соответствующую названию класса. 
Создать экземпляры классов и проверить работу методов.
'''


class MathOperations:

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def calc(self):
        print("Запуск операции")


class MySum(MathOperations):

    def calc(self):
        super().calc()
        print(
            f"Результат сложения {self.first_num} и {self.second_num}: {self.first_num + self.second_num}"
        )


class MySub(MathOperations):

    def calc(self):
        super().calc()
        print(
            f"Результат вычитания {self.first_num} и {self.second_num}: {self.first_num - self.second_num}"
        )


class MyMult(MathOperations):

    def calc(self):
        super().calc()
        print(
            f"Результат вычитания {self.first_num} и {self.second_num}: {self.first_num * self.second_num}"
        )


sum_operation = MySum(10, 5)
sum_operation.calc()

print('\n' + '=' * 20 + '\n')

sub_operation = MySub(10, 5)
sub_operation.calc()

print('\n' + '=' * 20 + '\n')

sub_operation = MyMult(10, 5)
sub_operation.calc()
