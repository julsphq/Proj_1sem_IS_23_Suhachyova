#Вариант 27.  В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.

import random
N = int(input("Введите номер строки N: "))
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица:")
for row in matrix:
    print(*row)

try:
    for i in range(len(matrix[N-1])):
        matrix[N-1][i] += 3
except IndexError:
    print(f"Введенный номер строки N выходит за пределы матрицы.")
else:
    print("Преобразованная матрица:")
    for row in matrix:
        print(*row)
