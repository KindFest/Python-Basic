# Урок 5. Практическое задание 4.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

from googletrans import Translator


# using dict ------------------------------
dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
ru_file = open('text_4_ru.txt', 'w', encoding='utf-8')
with open('text_4.txt', 'r', encoding='utf-8') as eng_f:
    for orig_str in eng_f:
        orig_str = orig_str.split()
        new_str = f'{dictionary[orig_str[0]]} - {orig_str[-1]}'
        print(new_str, file=ru_file)
ru_file.close()

# using Google Translator ---------------------------

translator = Translator()
ru_file_online = open('text_4_ru_online.txt', 'w', encoding='utf-8')
with open('text_4.txt', 'r', encoding='utf-8') as eng_f:
    for orig_str in eng_f:
        orig_str = orig_str.split()
        translated = translator.translate(orig_str[0], src='en', dest='ru')
        new_str = f'{translated.text.capitalize()} - {orig_str[-1]}'
        print(new_str, file=ru_file_online)
ru_file.close()
