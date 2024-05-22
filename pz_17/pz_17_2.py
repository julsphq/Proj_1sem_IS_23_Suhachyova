#Перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно.
# перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
#файлов в папке test.
# перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).
# перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
#привязанной к нему программе. Использовать функцию os.startfile().
# удалить файл test.txt.


import os

#os.chdir(r'C:\Users\Admin\PycharmProjects\Proj_1sem_IS_23_Suhachyova\pz_11')
#print(os.listdir())


#os.chdir("..")
#os.makedirs('test/test1')
#os.replace("pz_6/pz_6_1.py", "test/pz_6_1.py")
#os.replace("pz_6/pz_6_2.py", "test/pz_6_2.py")
#os.replace("pz_7/pz_7_1.py", "test/test1/pz_7_1.py")
#os.rename("test/test1/pz_7_1.py", "test/test1/test.txt")
#for file in os.listdir('test'):
  #if os.path.isfile(os.path.join("test", file)):
    #print(f"Размер файла '{file}': {os.path.getsize(os.path.join('test', file))} байт")


#os.chdir(r'C:\Users\Admin\PycharmProjects\Proj_1sem_IS_23_Suhachyova\pz_11')
#short_file = min((f for f in os.listdir()), key=lambda x: len(os.path.basename(x)))
#print(f"Файл с самым коротким именем: {os.path.basename(short_file)}")


#os.chdir(r'C:\Users\Admin\PycharmProjects\Proj_1sem_IS_23_Suhachyova\reports')
#os.startfile('pz_15.pdf')


#os.chdir("..")
#os.remove("test/test1/test.txt")