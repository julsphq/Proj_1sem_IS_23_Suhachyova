# Дан целочисленный список A размера N. Переписать в новый целочисленный
# список B все четные числа из исходного списка (в том же порядке) и вывести размер
# полученного список B и его содержимое.

def extract_numbers(arr):
    B = [num for num in arr if num % 2 == 0]
    print("Размер полученного списка B:", len(B))
    print("Содержимое списка B:", B)

A = [3, 8, 1, 7, 2, 9, 4, 6]
print(A)

extract_numbers(A)