# Вариант 27. Описать функцию AddRightDigit(D, K), добавляющую к целому положительному
# числу K справа цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 0-9, K — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу K справа
# данные цифры D1 и D2, выводя результат каждого добавления.

def AddRightDigit(D, K):
    try:
        for x in range(2):
            if int(D) > 0 and int(D) < 9:
                    K = f"{K}{D}"
                    print(K)
                    return K
            else:
                print('Число D не соответствует указанным параметрам, попробуйте заново!')
                AddRightDigit(D=input('Введите число D: '), K=input('Введите число K: '))

    except:
        print('Какое-то число было введено неверно, попробуйте заново')
        AddRightDigit(D=input('Введите число D: '), K=input('Введите число K: '))

B = AddRightDigit(D=input('Введите число D: '), K=input('Введите число K: '))
AddRightDigit(D=input('Введите число D: '), K=B)