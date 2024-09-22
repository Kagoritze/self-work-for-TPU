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
