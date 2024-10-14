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


def main():
    arr = [random.uniform(0, 1000) for i in range(1000)]
    print("Исходный массив:")
    print_array(arr)

    print("=" * 20)

    sorted_arr, elapsed_time = measure_time(selection_sort, arr.copy())
    print(f"Время сортировки выбором: {elapsed_time:.6f} секунд")

    sorted_arr, elapsed_time = measure_time(inserts_sort, arr.copy())
    print(f"Время сортировки вставками: {elapsed_time:.6f} секунд")

    sorted_arr, elapsed_time = measure_time(bubble_sort, arr.copy())
    print(f"Время сортировки пузырьком: {elapsed_time:.6f} секунд")

    sorted_arr, elapsed_time = measure_time(shell_sort, arr.copy())
    print(f"Время сортировки Шелла: {elapsed_time:.6f} секунд")

    sorted_arr, elapsed_time = measure_time(quick_sort, arr.copy())
    print(f"Время быстрой сортировки: {elapsed_time:.6f} секунд")

    print("=" * 20)

    print("Отсортированный массив:")
    print_array(sorted_arr)


def print_array(arr):
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
    for i in range(len(arr) - 1):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def inserts_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


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


def shell_sort(arr):
    last_index = len(arr)
    step = last_index // 2
    while step > 0:
        for i in range(step, last_index):
            temp = arr[i]
            j = i
            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = temp
        step //= 2


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    main()
