# Урок 3. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def divide_num(num1, num2):
    """Функция производит деление первого параметра на второй"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Деление на ноль запрещено!'


def input_digit():
    """Функция по вводу только чисел"""
    while True:
        try:
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))
            return num1, num2
        except ValueError:
            print('Надо вводить числа! Давайте еще раз.')


print('Программа делит первое число на второе')
number_1, number_2 = input_digit()
result = divide_num(number_1, number_2)
print(f'{number_1} / {number_2} = {result}' if type(result) != str else result)
