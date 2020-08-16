# Урок 7. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной
# схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22
# 37 43
# 51 86
#
# 3   5   32
# 2   4   6
# -1  64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

import random


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([[self.matrix[j][i] + other.matrix[j][i] for i in range(len(self.matrix[0]))]
                       for j in range((len(self.matrix)))])

    def __str__(self):
        """Создание строки простым перебором"""
        text = ''
        for row in self.matrix:
            for col in row:
                text += f'{col:> 5}'
            text += f'\n'
        return text

# Попытался оптимизировать код, но не могу сделать выравнивание, как в блоке выше
#     def __str__(self):
#         return '\n'.join([f'{"   ".join(map(str, row))}' for row in self.matrix])


def generate_matrix(row, col):
    return [[random.randrange(-99, 99) for _ in range(col)] for _ in range(row)]


matrix_1 = Matrix(generate_matrix(3, 2))
matrix_2 = Matrix(generate_matrix(3, 2))
print(f'Матрица 1: \n{matrix_1}')
print(f'Матрица 2: \n{matrix_2}')
print(f'Сумма матриц 1 и 2: \n{matrix_1 + matrix_2}')
