# Урок 3. Практическое задание 4.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
# оператора **. Второй — более сложная реализация без оператора **, предусматривающая
# использование цикла.

def my_pow1(num1, num2):
    """Решение с помощью опретора **"""
    return num1 ** num2


def my_pow2(num1, num2):
    """Решение с помощью цикла"""
    num = 1
    for i in range(abs(num2)):
        num *= num1
    return 1 / num


while True:
    try:
        x = int(input('Введите целое положительное число: '))
        y = int(input('Введите целое отрицательное число: '))
        if x > 0 > y:
            break
        else:
            print('Надо вводить числа согласно условиям!')
    except ValueError:
        print('Надо вводить числа согласно условиям!')

print(f'1й способ: {x} в степени {y} равно {my_pow1(x, y):.4}')
print(f'2й способ: {x} в степени {y} равно {my_pow2(x, y):.4}')
