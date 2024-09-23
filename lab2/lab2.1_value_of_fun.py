"""
Пысларь Никита, ИУ7-11Б, Вариант-4
Лабораторная работа #2, часть 2, з.1
Написать программу, которая по введенному значению аргумента определит значение функции у
"""

# Импорт модуля для математических операций
import math

# Получаем коофицент уравннеия
x = float(input("Введите значение x: "))

# Решение уравнения
if x <= -5:
    y = -x - 5  

elif -5 < x <= 0:
    y = x + 5 

elif 0 <= x < 5:
    y = math.sqrt(25 - x**2) 

elif x >= 5:
    y = math.log(x - 4, 10) 

else:
    y = None  

# Вывод значений
print("Значение y:", y)
