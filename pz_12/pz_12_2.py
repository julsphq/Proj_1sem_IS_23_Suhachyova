#2.Составить генератор (yield), который переведет символы строки из нижнего
#регистра в верхний.
def generator(stroka):
    for n in stroka:
        yield n.upper()

stroka = input('Введите строку: ')
result = generator(stroka)

print(''.join(result))

