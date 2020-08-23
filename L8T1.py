# Урок 8. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, my_string):
        self.my_string = my_string

    @classmethod
    def split_string(cls, str_to_deal):
        return cls.check(list(map(int, str_to_deal.split('-'))))

    @staticmethod
    def check(my_list):
        if 0 < my_list[0] < 31 and 0 < my_list[1] < 13 and 0 < my_list[2] < 9999:
            return 'Дата проверена успешно'
        else:
            return 'Введена некорректная дата'


d_1 = Data("21-1-2020")
print(d_1.split_string(d_1.my_string))
