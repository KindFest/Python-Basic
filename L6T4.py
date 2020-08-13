# Урок 6. Практическое задание 4.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
# SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
# показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
# show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.
import random


class Car:
    directions = ['Юг', 'Юго-Запад', 'Запад', 'Северо_Запад', 'Север', 'Северо-Восток', 'Восток',
                  'Юго-Восток']
    is_going = False

    def __init__(self, speed, name, color, is_police):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police
        print(f'Автомобиль {self.name} цвета {self.color} создан и ждет Вас!')

    def go(self):
        if self.speed > 0:
            print(f'Автомобиль {self.name} цвета {self.color} поехал.')
            self.is_going = True
        else:
            print(f'Введите скорость больше 0, чтобы автомобиль поехал.')

    def stop(self):
        if self.speed > 0:
            print(f'Автомобиль {self.name} цвета {self.color} остановился.')
            self.is_going = False
        else:
            print(f'Параметр "Скорость" должен быть > 0, чтобы выполнить это действие.')

    def turn(self):
        course = random.choice(self.directions)
        if self.is_going and self.speed > 0:
            print(f'Направление движения автомобиля {self.name}: {course}')
        else:
            print(f'Автомобиль {self.name} стоит носом в направлении {course} :).')

    def show_speed(self):
        if self.is_going:
            print(f'Скорость автомобиля {self.name} равна {self.speed}')
        else:
            print(f'Автомобиль {self.name} стоит. Скорость движения равна 0 км/ч')


class TownCar(Car):
    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)
    
    def show_speed(self):
        if self.is_going:
            print(f'Скорость автомобиля {self.name} равна {self.speed}')
            if self.speed > 60:
                print('Вы превысили разрешенную скорость в 60 км/ч!')
        else:
            print(f'Автомобиль {self.name} стоит. Скорость движения равна 0 км/ч')


class SportCar(Car):
    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)


class WorkCar(Car):
    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)

    def show_speed(self):
        if self.is_going:
            print(f'Скорость автомобиля {self.name} равна {self.speed}')
            if self.speed > 40:
                print('Вы превысили разрешенную скорость в 40 км/ч!')
        else:
            print(f'Автомобиль {self.name} стоит. Скорость движения равна 0 км/ч')


class PoliceCar(Car):
    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)


w1 = WorkCar(50, 'Work Car', 'Оранжевый', False)
w1.show_speed()
w1.turn()
w1.go()
w1.show_speed()
w1.turn()
w1.stop()
w1.show_speed()
t1 = TownCar(70, 'Town Car', 'Белый', False)
t1.show_speed()
t1.turn()
t1.go()
t1.show_speed()
t1.turn()
t1.stop()
t1.show_speed()
s1 = SportCar(150, 'Sport Car', 'Красный', False)
s1.show_speed()
s1.turn()
s1.go()
s1.show_speed()
s1.turn()
s1.stop()
s1.show_speed()
p1 = PoliceCar(60, 'Police Car', 'Синий', True)
p1.show_speed()
p1.turn()
p1.go()
p1.show_speed()
p1.turn()
p1.stop()
p1.show_speed()
