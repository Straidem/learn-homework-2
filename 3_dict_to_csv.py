"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list_of_dicts = [
        {'name': 'Bill', 'age': 23, 'job': 'programmer'},
        {'name': 'Jack', 'age': 44, 'job': 'economist'},
        {'name': 'Will', 'age': 31, 'job': 'writer'},
        {'name': 'Mike', 'age': 50, 'job': 'Builder'}
    ]

    with open('user.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for q in list_of_dicts:
            writer.writerow(q)



if __name__ == "__main__":
    main()