#Вариант 27. Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате

import pickle

class Student:
    def __init__(self, name, surname, evaluations):
        self.name = name
        self.surname = surname
        self.evaluations = evaluations

def save_student(student, filename):
    with open(filename, 'wb') as f:
        pickle.dump(student, f)

def load_student(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

st1 = Student("Юлия", "Сухачёва", [5, 5, 5, 5, 5])
st2 = Student("Данил", "Рычков", [5, 5, 4, 5, 4])
st3 = Student("Анастасия", "Лещенко", [4, 4, 4, 5, 5])

students = [st1, st2, st3]
save_student(students, 'STUDENT.bin')
loaded_students = load_student('STUDENT.bin')

for student in loaded_students:
    print(f'Имя: {student.name}, Фамилия: {student.surname}, Оценки: {student.evaluations}')
