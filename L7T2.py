# Урок 7. Практическое задание 2.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом
# проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу
# декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 44:
            self.__size = 44
        elif size > 56:
            self.__size = 56
        else:
            self.__size = size

    @property
    def get_fabric_quantity(self):
        return str(round(self.size / 6.5 + 0.5, 2))


class Suit(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 150:
            self.__height = 150
        elif height > 210:
            self.__height = 210
        else:
            self.__height = height

    @property
    def get_fabric_quantity(self):
        return str(round(2 * self.height / 100 + 0.3, 2))


coat_1 = Coat(50)
print(f'Для пошива пальто {coat_1.size}го размера требуется {coat_1.get_fabric_quantity} метров ткани.')
suit_1 = Suit(170)
print(f'Для пошива костюма с ростом {suit_1.height} см требуется {suit_1.get_fabric_quantity} метров ткани.')
