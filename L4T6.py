# Урок 4. Практическое задание 6.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение
# элементов списка будет прекращено.

import itertools


def my_count(begin, counts):
    for i in itertools.islice(itertools.count(begin), counts):
        print(i)


def my_cycle(text, counts):
    for el in itertools.islice(itertools.cycle(text), counts):
        print(el)


def func_together(begin, counts):
    for i in itertools.islice(itertools.count(begin), counts):
        print(next(my_iter))
        print(i)


my_count(3, 6)
print('-' * 50)
my_cycle('Я крут!', 10)
print('-' * 50)
my_iter = itertools.cycle('Я крут!')
func_together(2, 30)
