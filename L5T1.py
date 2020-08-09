# Урок 5. Практическое задание 1.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.
from os import path


print('Программа создания файла и записи информации в него')
exit_flag = False
choice = '1'
while not exit_flag:
    file_name = input('Введите имя файла: ')
    if path.exists(file_name):
        print('Такой файл уже существует. Выберите дальнейшее действие.')
        while True:
            choice = input('1 - для ввода нового имени, 2 - обнулить текущий файл, 3 - добавить в конец файла: ')
            if choice == '1':
                break
            elif choice == '2':
                file_name = open(file_name, 'w', encoding='UTF-8')
                exit_flag = True
                break
            elif choice == '3':
                file_name = open(file_name, 'a', encoding='UTF-8')
                exit_flag = True
                break
            else:
                print('Некорректный ввод. Повторите выбор.')
    else:
        file_name = open(file_name, 'w', encoding='UTF-8')
        exit_flag = True
while True:
    input_str = input('Введите строку для записи в файл или нажмите Enter для выхода.\n')
    if input_str != '':
        file_name.write(input_str + '\n')
    else:
        break
file_name.close()
