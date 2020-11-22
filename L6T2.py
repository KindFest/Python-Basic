# Урок 6. Практическое задание 2.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
# полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    weght_for_1_sq_m = 25
    thickness = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight(self):
        return self.__length * self.__width * self.weght_for_1_sq_m * self.thickness


def input_digit(text):
    """Функция по вводу только чисел"""
    while True:
        try:
            num1 = float(input(text))
            return num1
        except ValueError:
            print('Надо вводить числа! Давайте еще раз.')


length_route = input_digit('Введите длину дороги, м: ')
width_route = input_digit('Введите ширину дорог, м: ')
highway_66 = Road(length_route, width_route)
print(f'Для покрытия дорожного полотна требуется {highway_66.weight() / 1000:.2f} тн асфальта.')
