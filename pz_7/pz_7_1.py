# Вариант 27. Дан символ C и строка S. Удвоить каждое вхождение символа C в строку S
def double_char(s, c):
    result = ""  # Создаем пустую строку для результата
    for char in s:
        if char == c:
            result += char * 2
        else:
            result += char

    return result

input_string = "Hello, World!"
character = "o"
doubled_string = double_char(input_string, character)
print(doubled_string)

