"""
Реализовать программу, выполняющую операции сложения, умножения, деления и вычитания над любыми числами, 
при этом количество переменных должно быть не меньше трех. Программа должна производить вывод применяя 
три разных способа форматирования строк (Си-стиль, метод format, f-строки). 
А также программа должна преобразовывать тип вводимых значений из строкового в целые и вещественные числа с указанием количества знаков после запятой.
"""


def get_number_input(promt):
    pass


def main():
    num1 = get_number_input("Введите первое число: ")
    num2 = get_number_input("Введите второе число: ")
    num3 = get_number_input("Введите третье число: ")

    if num1 is None or num2 is None or num3 is None:
        print("Ошибка ввода, введена буква или есть лишние числа")
    else:
        sum_result = num1 + num2 + num3
        sub_result = num1 - num2 - num3
        mul_result = num1 * num2 * num3
        div_result = None
        if num2 != 0 and num3 != 0:
            div_result = num1 / num2 / num3

        print("\nСи-стиль:")
        print("Сумма: %.2f, Разность: %.2f, Произведение: %.2f" %
              (sum_result, sub_result, mul_result))
        if div_result is not None:
            print("Деление: %.2f" % div_result)
        else:
            print("Деление: невозможно (деление на 0)")

        print("\nМетод format:")
        print("Сумма: {:.2f}, Разность: {:.2f}, Произведение: {:.2f}".format(
            sum_result, sub_result, mul_result))
        if div_result is not None:
            print("Деление: {:.2f}".format(div_result))
        else:
            print("Деление: невозможно (деление на 0)")

        print("\nf-строки:")
        print(
            f"Сумма: {sum_result:.2f}, Разность: {sub_result:.2f}, Произведение: {mul_result:.2f}"
        )
        if div_result is not None:
            print(f"Деление: {div_result:.2f}")
        else:
            print("Деление: невозможно (деление на 0)")


def get_number_input(prompt):
    user_input = input(prompt)

    if user_input.isalpha() or not user_input or len(user_input.split()) > 1:
        return None

    return float(user_input) if '.' in user_input else int(user_input)


if __name__ == "__main__":
    main()