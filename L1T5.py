# 5. Анализ работы фирмы

revenue = int(input('Введите размер выручки компании: '))
costs = int(input('Введите сумму издержек компании: '))
if revenue - costs > 0:
    print(f'Компания получила прибыль {revenue - costs}')
    print(f'Рентабельность выручки составила {revenue / costs:.2f}')
    employees = int(input("Введите количество сотрудников компании: "))
    print(f'Прибыль на одного сотрудника составила: {(revenue - costs) / employees:.2f}')
else:
    print(f'Компания получила убыток {revenue - costs}')
