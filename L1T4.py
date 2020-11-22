# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в
# числе. Для решения используйте цикл while и арифметические операции.

print('Поиск наибольшей цифры в любом положительном числе')
while True:
    number = int(input('Введите любое число больше 0: '))
    if number > 0:
        break
origin_number = number
maximum = number % 10
number = number // 10
while number > 0:
    if number % 10 > maximum:
        maximum = number % 10
    number = number // 10

print(f'Максимальная цифра в числе {origin_number} является {maximum}')