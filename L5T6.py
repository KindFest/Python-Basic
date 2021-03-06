# Урок 5. Практическое задание 6.
# ФИО: Артур Назарян
# Курс: Основы языка Python
# Факультет: Geek University Python-разработки
#
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def exclude_parenthesis(str_les):
    return int(str_les[:str_les.index('(')])


result_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    content_list = f.readlines()
    for el in content_list:
        el = el.split()
        hours = 0
        for el_1 in el[1:]:
            if '(' in el_1:
                hours += exclude_parenthesis(el_1)
        result_dict.update({el[0][:-1]: hours})
print(result_dict)
