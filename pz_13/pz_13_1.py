#Вариант 27. 1. В матрице найти среднее арифметическое положительных элементов, кратных 3.

import random

m = random.randint(3, 5)
n = random.randint(3, 5)
matr= [[random.randint(-10, 10) for _ in range(n)] for _ in range(m)]
print("Исходная матрица:")
for row in matr:
    print(*row)

arithmetic = [num for row in matr for num in row if num > 0 and num % 3 == 0]

if arithmetic:
    average = sum(arithmetic) / len(arithmetic)
    print(f"Среднее арифметическое положительных элементов, кратных 3: {average}")
else:
    print("В матрице нет положительных элементов, кратных 3")
