# Урок 7. Практическое задание 3.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки

class Cell:
    def __init__(self, quantity):
        self.units = quantity

    def __add__(self, other):
        return f'Сложение: {self.units} + {other.units} = {self.units + other.units}'

    def __sub__(self, other):
        return f'Вычитание: {max(self.units, other.units)} - {min(self.units, other.units)} = ' \
               f'{max(self.units, other.units) - min(self.units, other.units)}'

    def __mul__(self, other):
        return f'Умножение: {self.units} * {other.units} = {self.units * other.units}'

    def __floordiv__(self, other):
        return f'Деление нацело: {max(self.units, other.units)} // {min(self.units, other.units)}' \
               f' = {max(self.units, other.units) // min(self.units, other.units)}'

    def make_order(self, rows):
        return f'Разбиение клетки на ряды. Количество символов в ряду {rows}\n' \
               + ''.join([(chr(9787) * rows + '\n') for _ in range(self.units // rows)])\
               + f'{chr(9787) * (self.units % rows)}'


cell_1 = Cell(5)
cell_2 = Cell(16)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
cell_1.units = 20
cell_3 = cell_1 // cell_2
print(cell_3)
print(cell_1.make_order(8))
