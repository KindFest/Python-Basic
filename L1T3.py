# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Введите любое целое число: ')
if int(number) < 0:
    negative = True
    number = str(int(number) * -1)
else:
    negative = False

number_1, number_2, number_3 = [int(number), int(number * 2), int(number * 3)]

if negative:
    number_1, number_2, number_3 = [number_1 * -1, number_2 * -1, number_3 * -1]

total = number_1 + number_2 + number_3
print(f'Сумма {number_1: d}{number_2:+d}{number_3:+d} = {total}')
