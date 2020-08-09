# Урок 5. Практическое задание 2.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

def words_count(string):
    string = string.split()
    return len(string)


str_num = 0
total_words = 0
with open('text_3.txt', 'r', encoding='UTF-8') as f_name:
    for content in f_name:
        str_num += 1
        print(f'{str_num}я строка содержит {words_count(content)} слов')
        total_words += words_count(content)
print(f'Всего в файле {str_num} строк и {total_words} слов.')
