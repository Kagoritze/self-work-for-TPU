import random
import time


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
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
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def print_array(arr):
    print([f"{x:.2f}"
           for x in arr])  # Форматированный вывод с 2 знаками после запятой


def measure_sorting_time(sort_function, arr):
    start_time = time.time()
    if sort_function == quick_sort:
        arr = sort_function(arr)  # Быстрая сортировка возвращает новый массив
    else:
        sort_function(arr)
    end_time = time.time()
    return arr, end_time - start_time


def main():
    arr = [random.uniform(0, 1000) for i in range(1001)]
    print("Исходный массив:")
    print_array(arr)

    # Сортировка методом пузырька
    sorted_arr, elapsed_time = measure_sorting_time(bubble_sort, arr.copy())
    print("\nСортировка пузырьком:")
    print_array(sorted_arr)
    print(f"Время сортировки: {elapsed_time:.6f} секунд")

    # Сортировка выбором
    sorted_arr, elapsed_time = measure_sorting_time(selection_sort, arr.copy())
    print("\nСортировка выбором:")
    print_array(sorted_arr)
    print(f"Время сортировки: {elapsed_time:.6f} секунд")

    # Сортировка вставками
    sorted_arr, elapsed_time = measure_sorting_time(insertion_sort, arr.copy())
    print("\nСортировка вставками:")
    print_array(sorted_arr)
    print(f"Время сортировки: {elapsed_time:.6f} секунд")

    # Сортировка Шелла
    sorted_arr, elapsed_time = measure_sorting_time(shell_sort, arr.copy())
    print("\nСортировка Шелла:")
    print_array(sorted_arr)
    print(f"Время сортировки: {elapsed_time:.6f} секунд")

    # Быстрая сортировка
    sorted_arr, elapsed_time = measure_sorting_time(quick_sort, arr.copy())
    print("\nБыстрая сортировка:")
    print_array(sorted_arr)
    print(f"Время сортировки: {elapsed_time:.6f} секунд")


if __name__ == "__main__":
    main()
