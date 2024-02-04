#Вариант 27.
#1.В последовательности из N чисел (N –четное) в первой ее половине найти
#произведение элементов меньших 0.

import random
from functools import reduce

N = int(input("Введите длину последовательности (!ЧЁТНОЕ!): "))
A = [random.randint(-100, 100) for _ in range(N)]
print('Последовательность: ', A)

A1 = A[:len(A)//2]
A2 = list(filter(lambda x: x < 0, A1))

if A2:
    result = reduce(lambda x, y: x * y, A2)
    print('Произведение элементов меньше нуля в первой половине:', result)
else:
    print('Все элементы в первой половине положительные')



