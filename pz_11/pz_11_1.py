#Вариант 27.
#1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Элементы первого файла, присутствующие во втором:
#Элементы второго файла, присутствующие в первом:
#Количество элементов:
#Количество отрицательных элементов:
#Количество положительных элементов:

from random import randint

list1 = []   # Заполняем список рандомным количеством рандомных чисел.
for i in range(randint(5, 20)):
    list1.append(str(randint(-10, 10)))

list2 = []
for i in range(randint(5, 20)):
    list2.append(str(randint(-10, 10)))


f1 = open("file1.txt", "w+")
f2 = open("file2.txt", "w+")

s1 =" ".join(list1)
s2 =" ".join(list2)

f1.writelines(s1)
f2.writelines(s2)

f1.close()
f2.close()

f1 = open("file1.txt","r+")
f2 = open("file2.txt", "r+")

new_list1 = f1.read().split()
new_list2 = f2.read().split()
f1.close()
f2.close()

main_file = open("main.txt","w+")
f1 = open("file1.txt","r+")
f2 = open("file2.txt", "r+")
elements_present_in_second = [x for x in new_list1 if x in new_list2]
main_file.writelines(f"Элементы первого и второго файлов:\n"
                     f"{' '.join(new_list1)}\n"
                     f"{' '.join(new_list2)}\n\n"
                     f"Элементы первого файла, присутствующие во втором:\n"
                     f"{' '.join(elements_present_in_second)}\n"
                     f"Элементы второго файла, присутствующие в первом\n"
                     f"{' '.join([x for x in new_list2 if x in new_list1])}\n"
                     f"Количество элементов:\n"
                     f"{len(new_list1) + len(new_list2)}\n"
                     f"Количество отрицательных элементов:\n"
                     f"{sum(1 for x in new_list1 + new_list2 if int(x) < 0)}\n"
                     f"Количество положительных элементов:\n"
                     f"{sum(1 for x in new_list1 + new_list2 if int(x) > 0)}\n")
main_file.close()
f1.close()
f2.close()
