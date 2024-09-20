'''
Реализовать следующие алгоритмы сортировки:

    Сортировка выбором;
    Сортировка вставками;
    Сортировка “Методом пузырька”;
    Сортировка Шелла;
    Быстрая сортировка.

Программа должна сгенерировать список случайных неотсортированных чисел и вывести его на экран.

Затем этот список должен быть отсортирован каждым из пяти перечисленных выше алгоритмов сортировки. 
Необходимо также зафиксировать время работы каждого алгоритма сортировки и при выводе отсортированного массива на экран выводить время его сортировки.
'''

import random
import time


def measure_time():
    pass


def selection_sort(arr):
    pass


def inserts_sort(arr):
    pass


def bubble_sort(arr):
    pass


def shell_sort(arr):
    pass


def quick_sort(arr):
    pass


def main():
    arr = [random.uniform(0, 1000) for i in range(0, 1001)]
    bubble_sort(arr)
    print([f"{x:.2f}" for x in arr])


def measure_time(sort_function, arr):
    start_time = time.time()
    if sort_function == quick_sort:
        arr = sort_function(arr)
    else:
        sort_function(arr)
    end_time = time.time()
    return arr, end_time - start_time


def selection_sort(arr):
    pass


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    main()
