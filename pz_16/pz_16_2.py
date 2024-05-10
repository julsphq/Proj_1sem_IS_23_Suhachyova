#Вариант 27. Создайте класс "Автомобиль", который содержит информацию о марке, модели и
#годе выпуска. Создайте класс "Грузовик", который наследуется от класса
#"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
#"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
#информацию о количестве пассажиров.

class Avto:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Truck(Avto):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity

class Passenger(Avto):
    def __init__(self, brand, model, year, passengers):
        super().__init__(brand, model, year)
        self.passengers = passengers

car1 = Truck("Tesla", "Tesla Semi", 2017, 37000)
car2 = Passenger("BMW Motorsport", "BMW M5", 2021, 5)

print("Грузовик:", car1.brand, car1.model, car1.year, "\nГрузоподъемность:", car1.capacity,"\n")
print("Легковой автомобиль:", car2.brand, car2.model, car2.year, "\nКоличество пассажиров:", car2.passengers)

