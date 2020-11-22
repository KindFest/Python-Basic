# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print('Программа по переводу секунд в привычный формат времени')
while True:
    input_seconds = int(input('Введите количество секунд больше 0: '))
    if input_seconds > 0:
        break
hours = input_seconds // 3600
minutes = input_seconds % 3600 // 60
seconds = input_seconds % 3600 % 60

print(f'{input_seconds} секунд равно {hours:02d}ч:{minutes:02d}м:{seconds:02d}с')
