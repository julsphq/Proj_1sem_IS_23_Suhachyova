#Вариант 27
#Приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации. БД должна
#содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
#единицу измерения (штуки, килограммы, литры), количество, стоимость.

import sqlite3
from data import datas

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Sales(
        Surname TEXT NOT NULL,
        Name TEXT NOT NULL,
        Patronymic TEXT,
        Product TEXT NOT NULL,
        Unit_measurement TEXT NOT NULL,
        Quantity INTEGER NOT NULL,
        Price INTEGER NOT NULL 
        )""")

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.executemany("INSERT INTO Sales VALUES (?,?,?,?,?,?,?)", datas)

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT  * FROM Sales")
    for result1 in cursor.fetchall():
        print('Выборка 1 >>>', result1)

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Sales WHERE Patronymic = 'Викторович'")
    for result2 in cursor.fetchall():
        print('Выборка 2 >>>', result2)

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Sales WHERE Unit_measurement = 'штуки' AND Quantity >= 1")
    for result3 in cursor.fetchall():
        print('Выборка 3 >>>', result3)

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("UPDATE Sales SET Name = 'Виктория' WHERE Name LIKE 'Юлия' ")

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("UPDATE Sales SET  Quantity  = 17 WHERE  Quantity LIKE 5 ")

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("UPDATE Sales SET Price = 350, Quantity = 5 WHERE Price > 400"  )

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Sales WHERE Quantity > 15")

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Sales WHERE Unit_measurement = 'литры' ")

with sqlite3.connect('internet_shop.db') as connect:
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Sales WHERE  Price > 100 ")












