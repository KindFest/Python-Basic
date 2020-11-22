# 6. Задача про спортсмена

distance = float(input("Введите пройденную дистанцию за 1й день, км: "))
goal = float(input("Введите цель, км: "))
i = 1

while distance < goal * 1.1:
    print(f'{i}-й день: {distance:.2f}')
    i += 1
    distance *= 1.1

print(f'Ответ: на {i-1}-й день спортсмен достиг цели — не менее {goal} км.')
