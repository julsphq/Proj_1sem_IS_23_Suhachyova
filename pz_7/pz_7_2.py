# Вариант 27. Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти количество слов в строке.

def count_words(string):
    string = string.split()
    print(f'Пробелов в строке: {len(string) - 1}')


if __name__ == '__main__':
    main(count_words= input('Введите строку: '))