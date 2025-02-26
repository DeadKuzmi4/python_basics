"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

number_user = int(input("Введите целое положительное число: "))

max_element = number_user % 10
number_user = number_user // 10
while number_user > 0:
    if number_user % 10 > max_element:
        max_element = number_user % 10
    number_user = number_user // 10
print(f"Самая большая цифра в числе: {max_element}")