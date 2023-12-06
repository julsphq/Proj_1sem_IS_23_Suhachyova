# Вариант 27. Составить программу, в которой функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры.

import random
def check_duplicate_digits():
    number = random.randint(1000, 9999)
    print("Сгенерированное число:", number)

    digits = [int(x) for x in str(number)]
    unique_digits = set(digits)

    if len(digits) != len(unique_digits):
        print("В числе есть одинаковые цифры")
    else:
        print("В числе нет одинаковых цифр")

check_duplicate_digits()
