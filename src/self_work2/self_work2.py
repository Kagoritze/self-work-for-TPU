'''
Цель работы:

Обрести навыки применения условной инструкции и усовершенствовать навыки работы с математическими операторами.

Задачи:

Напишите программу для решения восьми уравнений, приведенных под номерами с 1-го по 8-й. Предусмотрите проверку деления на ноль с помощью оператора if.
Все необходимые переменные пользователь вводит через консоль. Вывод результата оформить с помощью f-строк.

Для выполнения работы вам понадобится библиотека math. Подключить её можно с помощью команды: import math в самом начале программы.
'''
import math


def main():
    x = get_number_input("Введите число x: ")
    y = get_number_input("Введите число y: ")
    z = get_number_input("Введите число z: ")

    if x is None or y is None or z is None:
        print("Ошибка ввода, введена буква или есть лишние символы\n")
    else:
        denominator = z + x**2 / 4

        if denominator == 0:
            print("Ошибка: деление на ноль в уравнении 1\n")
        else:
            numerator = abs(y - math.sqrt(abs(x))) * (x - y / denominator)
            if numerator <= 0:
                print("Ошибка: аргумент для логарифма равен 0 в уравнении 1\n")
            else:
                k = math.log(numerator / denominator)
                print(f"Результат уравнения 1: k = {k}\n")

    x = get_number_input("Введите число x: ")
    y = get_number_input("Введите число y: ")
    if x is None or y is None:
        print("Ошибка ввода, введена буква или есть лишние символы\n")
    else:
        d = (2 * math.cos(x - math.pi / 6) / (1 / 2 + pow(math.sin(y), 2)) +
             abs(y - x) / 3)
        print(f"Результат уравнения 2: d = {d}\n")

    x = get_number_input("Введите число x: ")
    y = get_number_input("Введите число y: ")
    if x is None or y is None:
        print("Ошибка ввода, введена буква или есть лишние символы\n")
    else:
        numerator = (x / y) * (z + x) * math.exp(abs(x - y)) + math.log(1 +
                                                                        math.e)
        denominator = pow(math.sin(y), 2) - pow(math.sin(x) * math.sin(y), 2)
        if denominator == 0:
            print("Ошибка: деление на ноль в уравнении 3\n")
        else:
            w = numerator / denominator
            print(f"Результат уравнения 3: w = {w}\n")

    x = get_number_input("Введите число x: ")
    y = get_number_input("Введите число y: ")
    z = get_number_input("Введите число z: ")
    if x is None or y is None or z is None:
        print("Ошибка ввода, введена буква или есть лишние символы\n")
    else:
        if 1 + pow(x, 2) * abs(y - math.tan(z)) == 0:
            print("Ошибка: деление на ноль в уравнении 4\n")
        else:
            b = (3 + math.exp(y - 1)) / (1 + pow(x, 2) * abs(y - math.tan(z)))
            print(f"Результат уравнения 4: b = {b}\n")

        a = get_number_input("Введите число a: ")
        b = get_number_input("Введите число b: ")
        c = get_number_input("Введите число c: ")
        if a * b < -2:
            p = math.sqrt(abs(a * b)) + 2 * c
        elif -2 <= a * b <= 2:
            p = a**3 + b**2 - c**2
        else:
            p = a**c - b
        print(f"Результат уравнения 5: p = {p}\n")

    x = get_number_input("Введите число x: ")
    y = get_number_input("Введите число y: ")
    if x is None or y is None:
        print("Ошибка ввода, введена буква или есть лишние символы\n")
    else:
        if x < y:
            h = math.atan(x + abs(y))
        elif x > y:
            h = math.atan(abs(x) + y)
        else:
            h = (x + y)**2
        print(f"Результат уравнения 6: h = {h}\n")

    x = get_number_input("Введите число x: ")
    y = get_number_input("Введите число y: ")
    if x is None or y is None:
        print("Ошибка ввода, введена буква или есть лишние символы\n")
    else:
        if x / y > 0:
            b = math.log(x / y) + (x**2 + y)**3
        elif x / y < 0:
            b = math.log(abs(x / y)) + (x**2 + y)**3
        elif x == 0 and y != 0:
            b = (x**2 + y)**3
        else:
            b = 0
        print(f"Результат уравнения 7: b = {b}\n")

    x = get_number_input("Введите число x: ")
    y = get_number_input("Введите число y: ")
    if x is None or y is None:
        print("Ошибка ввода, введена буква или есть лишние символы\n")
    else:
        if x - y > 0:
            b = math.sin(x + y) + 2 * (x + y)**2
        elif x - y < 0:
            b = math.sin(x - y) + (x - y)**3
        elif x == 0 and y != 0:
            b = abs(x**2 + math.sqrt(y))
        else:
            b = 0
        print(f"Результат уравнения 8: b = {b}\n")


def get_number_input(prompt):
    user_input = input(prompt)

    if user_input.isalpha() or not user_input or len(user_input.split()) > 1:
        return None

    return float(user_input) if '.' in user_input else int(user_input)


if __name__ == "__main__":
    main()
