"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dn_now = datetime.now()
    dn_yes = timedelta(days=1)
    dn_yes_fr = dn_now - dn_yes
    dn_30d = timedelta(days=30)
    dn_30d_fr = dn_now - dn_30d
    print(f'сегодня:{dn_now.strftime("%d.%m.%Y")}')
    print(f'вчера: {dn_yes_fr.strftime("%d.%m.%Y")}')
    print(f'30 дней назад: {dn_30d_fr.strftime("%d.%m.%Y")}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_tm = datetime.strptime(date_string,"%d/%m/%y %H:%M:%S.%f")
    return date_tm.strftime("%d.%m.%Y %H:%M:%S.%f")


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
