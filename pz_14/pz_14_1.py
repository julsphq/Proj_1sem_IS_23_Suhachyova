#Вариант 27. Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
#год и поместить ее в новый текстовый файл.

import re

with open('Dostoevsky.txt', encoding='utf-8') as file:
    text = file.read()

pattern = re.compile(r"После .*", re.MULTILINE)
matches = pattern.findall(text)

with open('newfile.txt', 'w', encoding='utf-8') as file:
    file.writelines(matches)

