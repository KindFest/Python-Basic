# Урок 6. Практическое задание 5.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три
# дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для
# каждого экземпляра.

class Stationery:
    title = 'Канцелярка'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    title = 'Маркер'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


s = Stationery()
s.draw()
p = Pen()
p.draw()
pnc = Pencil()
pnc.draw()
h = Handle()
h.draw()
print(dir(p))
