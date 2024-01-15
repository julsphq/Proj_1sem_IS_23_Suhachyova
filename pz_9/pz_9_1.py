#Вариант 27. Организовать словарь на 10 англо-русских слов, обеспечивающий
#"перевод" английского слова на русский.

dictionary = {
    "land": "земля",
    "house": "дом",
    "world": "мир",
    "programmer": "программист",
    "car": "машина",
    "teacher": "учитель",
    "software": "программное обеспечение",
    "college": "колледж",
    "tree": "дерево",
    "sea": "море"
}

word = input("Введите слово на английском: ")
if word in dictionary:
    translation = dictionary[word]
    print("Перевод слова", word, "на русский:", translation)
else:
    print("Перевод для этого слова не найден")
