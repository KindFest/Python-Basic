# Урок 6. Практическое задание 3.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на
# словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать
# класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить
# работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name_w, surname_w, position_w, income_w):
        self.name = name_w
        self.surname = surname_w
        self.position = position_w
        self.__income = income_w


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._Worker__income.values())


def input_digit(text):
    """Функция по вводу только чисел"""
    while True:
        try:
            num1 = float(input(text))
            return num1
        except ValueError:
            print('Надо вводить числа! Давайте еще раз.')


w1 = Position('Иван', 'Иванов', 'менеджер', {"wage": 100000, "bonus": 10000})
w2 = Position('Петр', 'Петров', 'менеджер', {"wage": 20000, "bonus": 500})
w3 = Position('Сергей', 'Сергеев', 'менеджер', {"wage": 5000, "bonus": 78000})
name = input('Введите имя: ')
surname = input('Введте фамилию: ')
position = input('Введите должность: ')
salary = input_digit('Введите оклад: ')
bonus = input_digit('Введите премию: ')
w4 = Position(name, surname, position, {"wage": salary, "bonus": bonus})
emploees = [w1, w2, w3, w4]
for emploee in emploees:
    print(f'Сотрудник: {emploee.get_full_name():>30}')
    print(f'Позиция: {emploee.position:>32}')
    print(f'Сококупный доход: {emploee.get_total_income():>23}')
