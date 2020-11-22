# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

number_1 = 1
number_2 = number_1 +5
string_1 = 'Hello'
string_2 = string_1 + ' world!'
print(string_2)
print(number_2 - number_1)
name = input('Как вас зовут? ')
number_3 = int(input(f'{name}, введите любое число от 1 до 10: '))
if 1 <= number_3 <= 10:
    if number_3 > number_2:
        print(f'{name}, ваше число {number_3} круче моего числа {number_2}!')
    elif number_3 < number_2:
        print(f'{name}, ваше число {number_3} бито моим числом {number_2}')
    else:
        print('Мы с вами на одной волне - числа равны!')
else:
    print(f'{name}, вы жульничаете и ввели неправильное число!')
