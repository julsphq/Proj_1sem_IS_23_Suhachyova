# Вариант 27.  Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
# наибольший периметр треугольника, вершины которого принадлежат различным
# точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором
# они перечислены при задании множества A).
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2
# Для хранения данных о каждом наборе точек следует использовать по два список: первый
# список для хранения абсцисс, второй — для хранения ординат.

import itertools
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Расстояние между точками по формуле
def find_perimeter(A):
    max_perimeter = 0
    max_triangle = []

    for i, j, k in itertools.combinations(range(len(A)), 3):
        a = distance(A[i][0], A[i][1], A[j][0], A[j][1])  # Расстояние между точками i и j
        b = distance(A[i][0], A[i][1], A[k][0], A[k][1])  # Расстояние между точками i и k
        c = distance(A[j][0], A[j][1], A[k][0], A[k][1])  # Расстояние между точками j и k

        # Вычисляем периметр треугольника
        perimeter = a + b + c

        if perimeter > max_perimeter:
            max_perimeter = perimeter
            max_triangle = [A[i], A[j], A[k]]

    return max_perimeter, max_triangle

A = [(0, 1), (1, 3), (4, 1), (2, 3)]
print(A)

result_perimeter, result_triangle = find_perimeter(A)

print("Наибольший периметр треугольника:", result_perimeter)
print("Вершины треугольника:", result_triangle)
