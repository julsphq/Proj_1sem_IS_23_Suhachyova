#Вариант 27. Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
#Добавьте методы для вычисления среднего балла и определения, является ли студент
#отличником
class Student:
    def __init__(self, name, surname, evaluations):
        self.name = name
        self.surname = surname
        self.evaluations = evaluations

    def average_evaluations(self):
        return sum(self.evaluations) / len(self.evaluations)

    def excellent_student(self):
        return all(evaluations >= 5 for evaluations in self.evaluations)

st1 = Student("Юлия", "Сухачёва", [5, 5, 5, 5, 5])
st2 = Student("Данил","Рычков",[5, 5, 4, 5, 4])
st3 = Student("Анастасия","Лещенко",[4, 4, 4, 5, 5])

print(st1.__dict__)
print(st2.__dict__)
print(st3.__dict__)

print("Средний балл студента:", st1.average_evaluations())
print("Средний балл студента:", st2.average_evaluations())
print("Средний балл студента:", st3.average_evaluations())

print("Студент отличник?", st1.excellent_student())
print("Студент отличник?", st2.excellent_student())
print("Студент отличник?", st3.excellent_student())