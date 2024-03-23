#Вариант 27. Из исходного текстового файла (Dostoevsky.txt) выбрать информацию,которая начинается с 1857
#года и поместить ее в новый текстовый файл

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    data = file.read()

pattern = re.compile(r'1857(.*?)(?=185\d{2}|$)', re.DOTALL)
match = pattern.search(data)

if match:
    info_1857 = match.group(0)
    with open('new_fille.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(info_1857)
        print("Информация за 1857 год успешно сохранена в файл 'new_fille.txt'")
else:
    print("Информация за 1857 год не найдена в исходном файле")
