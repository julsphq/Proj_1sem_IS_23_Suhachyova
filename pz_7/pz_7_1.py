# Вариант 27. Дан символ C и строка S. Удвоить каждое вхождение символа C в строку S
def main(C,S):
    try:
        temp_list = []
        for char in S:
            if not char == C:
                temp_list.append(char)
            else:
                temp_list.append(char*2)

        our_str = ''.join(temp_list)
        return our_str

    except:
        print('Что-то пошло не так, попробуйте еще раз!')
        print(main(C=input('Введите C: '), S=input('Введите S: ')))


if __name__ == '__main__':
    print(main(C=input('Введите C: '), S=input('Введите S: ')))
