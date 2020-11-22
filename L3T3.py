# Урок 3. Практическое задание 3.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def input_digit():
    """Функция по вводу только чисел"""
    while True:
        try:
            num1 = int(input('Введите число: '))
            return num1
        except ValueError:
            print('Надо вводить числа! Давайте еще раз.')


# Первый метод - сначала реализовал его и только потом меня осенило :)
# решил оставить его для истории )))
def my_func1(num1, num2, num3):
    list_num = [num1, num2, num3]
    list_num.remove(min([num1, num2, num3]))
    return list_num[0] + list_num[1]


# Второй метод
def my_func2(num1, num2, num3):
    return sum([num1, num2, num3]) - min(num1, num2, num3)


print(f'Сумма наибольших чисел = {my_func1(4, 5, 3)}')
print(f'Сумма наибольших чисел = {my_func2(input_digit(), input_digit(), input_digit())}')
