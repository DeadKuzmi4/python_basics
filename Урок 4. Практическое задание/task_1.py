"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""


def my_func(a,b, prize):
    return (a * b) + prize
print(my_func(12, 50, 1000))
'''
a = выработка в  часах
b = ставка в час
prize = премия
'''