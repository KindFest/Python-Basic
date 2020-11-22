# Урок 5. Практическое задание 5.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random


def input_digit():
    """Функция по вводу только чисел"""
    while True:
        try:
            num1 = int(input('Введите количество чисел, которое будет содержать файл: '))
            return num1
        except ValueError:
            print('Надо вводить числа! Давайте еще раз.')


def create_f(count, name_f):
    numb_list = [random.randint(-10, 10) for _ in range(count)]
    numb_str = ' '.join(map(str, numb_list))
    with open(name_f, 'w', encoding='utf-8') as f:
        print(numb_str, file=f)


def amount_f(name_f):
    with open(name_f, 'r', encoding='utf-8') as f:
        numbs = f.read()
    numbs = list(map(int, numbs.split()))
    total = 0
    for el in numbs:
        total += el
    print(f'Сумма чисел в файле {name_f} равна {total}')


file_name = input('Введите имя файла: ')
create_f(input_digit(), file_name)
amount_f(file_name)
