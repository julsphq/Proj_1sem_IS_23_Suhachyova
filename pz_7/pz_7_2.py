# Вариант 27. Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Найти количество слов в строке.

def count_words(input_string):
    words = input_string.split()
    return len(words)

input_string = "Пробелов в данной строке"
word_count = count_words(input_string)
print("Количество слов в строке:", word_count)  # Выводим результат
