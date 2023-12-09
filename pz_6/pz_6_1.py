# Вариант 27.  Дан список A размера N. Найти минимальный элемент из его элементов с четными
# номерами: A2, A4, A6, ... .

def min_index_element(arr):
    min_element = arr[1]
    for i in range(3, len(arr), 2):
        if arr[i] < min_element:
            min_element = arr[i]
    return min_element

A = [5, 3, 8, 2, 9, 6, 4,]
print(A)
result = min_index_element(A)
print("Минимальный элемент с чётным индексом:",result)

