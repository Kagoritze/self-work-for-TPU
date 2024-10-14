"""
1. Создать или загрузить таблицу с данными для аппроксимации и прогноза. Постарайтесь подобрать данные, связанные с вашей основной специальностью или научной работой.

2. Построить три различных аналитических графика с помощью библиотеки matplotlib.

3. Написать функции, вычисляющие коэффициенты m и c линейной регрессии методом наименьших квадратов, по загруженным/созданным данным.

4. Вывести линию тренда, полученную с помощью МНК.

5. Расширить список значений x и спрогнозировать значения y с помощью полученной линии тренда. Результат отобразить на отдельном графике.

http://www.cleverstudents.ru/articles/mnk.html
"""

import matplotlib.pyplot as plt
import numpy as np


def linear_regression(x, y):
    n = len(x)
    m = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (
        n * np.sum(x**2) - np.sum(x) ** 2
    )
    c = (np.sum(y) - m * np.sum(x)) / n
    return m, c


def main():
    np.random.seed(42)
    x = np.linspace(1, 10, 10)
    y = 2 * x + 3 + np.random.randn(10)

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.scatter(x, y, color="blue")
    plt.title("Исходные данные")
    plt.xlabel("x")
    plt.ylabel("y")

    m, c = linear_regression(x, y)

    y_pred = m * x + c

    plt.subplot(3, 1, 2)
    plt.scatter(x, y, color="blue", label="Исходные данные")
    plt.plot(x, y_pred, color="red", label="Линия тренда")
    plt.title(f"Линейная регрессия: y = {m:.3f}x + {c:.3f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    x_extended = np.linspace(1, 15, 15)
    y_extended = m * x_extended + c

    plt.subplot(3, 1, 3)
    plt.scatter(x_extended, y_extended, color="green", label="Прогноз")
    plt.title("Прогнозирование новых значений")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    plt.tight_layout()
    plt.show()
    # plt.savefig("output.png")

if __name__ == "__main__":
    main()
