# Урок 6. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
#  running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
#  светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
#  составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
#  зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

import tkinter


class TrafficLight:
    __color = ['red', 'yellow', 'green']
    p = {1: 125, 2: 135, 3: 125, 4: 246, 5: 125, 6: 361}
    r = 50

    # def __init__(self, x, y, r):
    #     self.x = x
    #     self.y = y
    #     self.r = r

    def running(self, num1, num2, num3, num4):
        canvas.create_oval(self.p[num1] - self.r, self.p[num2] - self.r,
                           self.p[num1] + self.r, self.p[num2] + self.r,
                           fill=self.__color[step], outline=self.__color[step])
        canvas.create_oval(self.p[num3] - self.r, self.p[num4] - self.r,
                           self.p[num3] + self.r, self.p[num4] + self.r,
                           fill='grey', outline='grey')


def main():
    global step, delay_time
    if step == 0:
        main_ball.running(1, 2, 5, 6)
        delay_time = 3000
        step = 1
    elif step == 1:
        main_ball.running(3, 4, 1, 2)
        step = 2
        delay_time = 1000
    elif step == 2:
        main_ball.running(5, 6, 3, 4)
        step = 0
        delay_time = 3000
    root.after(delay_time, main)


root = tkinter.Tk()
root.title("Traffic Light")
canvas = tkinter.Canvas(root, width=250, height=500, bg='blue')
canvas.create_rectangle(60, 80, 190, 420, fill='grey', outline='black', width=5)
canvas.create_line(60, 190, 190, 190, fill='black', width=5)
canvas.create_line(60, 305, 190, 305, fill='black', width=5)
canvas.pack()
step = 0
delay_time = 0
main_ball = TrafficLight()
main()
root.mainloop()
