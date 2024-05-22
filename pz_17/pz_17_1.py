#Вариант 27. Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ № 2 – 9. Для решения задачи использовала задачу №2 из ПЗ 3:
# Дан номер месяца — целое число в диапазоне 1-12 (1 — январь, 2 — февраль и т. д.).
# Вывести название соответствующего времени года («зима», «весна», «лето»,
# «осень»).

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_season():
    try:
        month = int(entry.get())
        if month in [1, 2, 12]:
            messagebox.showinfo("Время года", "Зима")
        elif month in [3, 4, 5]:
            messagebox.showinfo("Время года", "Весна")
        elif month in [6, 7, 8]:
            messagebox.showinfo("Время года", "Лето")
        elif month in [9, 10, 11]:
            messagebox.showinfo("Время года", "Осень")
        else:
            messagebox.showerror("Ошибка", "Ошибка ввода номера месяца. Введите число от 1 до 12.")
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный тип данных!")

window = tk.Tk()
window.title("Определение времени года")
window.geometry("500x800")

image = Image.open("кот.jpg")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(window, text="Введите номер месяца:", bg="#EEEEEE", font=("Arno Pro", 16))
label.pack(pady=10)
entry = tk.Entry(window, width=15, font=("Arial", 12))
entry.pack()

button = tk.Button(window, text="Определить время года", command=show_season, bg="#FFAACC", fg="white", font=("Arno Pro", 12, "bold"))
button.pack(pady=10)

window.mainloop()
