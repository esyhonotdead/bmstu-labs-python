"""
Пысларь Никита, ИУ7-11Б
Лабараторная работа #3
Задание:

1) Написать программу, которая по введенным целочисленным
координатам трех точек на плоскости вычисляет длины сторон
образованного треугольника и длину высоты, проведенной из
наименьшего угла.
2) Определить, является ли треугольник прямоугольным.
Далее вводятся координаты точки. Определить, находится ли точка
внутри треугольника. Если да, то найти расстояние от точки до
наиболее удаленной стороны треугольника или ее продолжения
"""

from math import sqrt, acos, degrees, cos

# Ввод координат точек
x1, y1 = int(input("Введите точку x1: ")), int(input("Введите точку y1: ")) #A
x2, y2 = int(input("Введите точку x2: ")), int(input("Введите точку y2: ")) #B
x3, y3 = int(input("Введите точку x3: ")), int(input("Введите точку y3: ")) #C

# Вычисление сторон треугольника
AB = sqrt((x2-x1)**2 + (y2-y1)**2) #AB
BC = sqrt((x3-x2)**2 + (y3-y2)**2) #BC
AC = sqrt((x3-x1)**2 + (y3-y1)**2) #AС
min_side = min(AB,BC,AC)

# Находим площадь треугольника
half_perimeter = AB + BC + AC
triangle_area = sqrt(half_perimeter*(half_perimeter-AB)*(half_perimeter-BC)*(half_perimeter-AC)) # Формула Герона

# Нахождение наименьшей высоты
height_A = 2 * triangle_area / BC 
height_B = 2 * triangle_area / AC
height_C = 2 * triangle_area / AB
if min_side == AB:
    height = height_C
elif min_side == BC:
    height = height_A
else:
    height = height_B


# Определяем является ли треугольник прямоугольным
is_sqare = False
if AB**2 == BC**2 + AC**2 or BC**2 == AC**2 + AB**2 or AC**2 == AB**2 + BC**2:
    is_sqare = True

# Определяем принадлженость точки треугольнику
x0, y0 = int(input("Введите точку x0: ")), int(input("Введите точку y0: "))

is_belong = False
# Тут описаны уравнения прямой
line_equation1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
line_equation2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
line_equation3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)

# Сравнание в 1 случае или лежит на стороне или за треугольнком, в 2 случае или в внутри или лежит на стороне
if ((line_equation1 >= 0 and line_equation2 >= 0 and line_equation3 >= line_equation3) or (line_equation1 <= 0 and line_equation2<= 0 and line_equation3 <=0)):
    is_belong = True

# Вычисление расстояния от точки до каждой из сторон (я сам не понимаю что делает этот код)
if is_belong == True:
    dist_ab = abs((y2 - y1) * x0 - (x2 - x1) * (y0 + x2) * y1 - y2 * x1) / AB
    dist_bc = abs((y3 - y2) * x0 - (x3 - x2) * (y0 - y2) + x3 * y2 - y3 * x2) / BC
    dist_ac = abs((y1 - y3) * x0 - (x1 - x3) * (y0 - y3) + x1 * y3 - y1 * x3) / AC
    max_dist = max(dist_ab, dist_bc, dist_ac)

#Вывод
print(f"Стороны AB={AB:.2g}")
print(f"Стороны BC={BC:.2g}")
print(f"Стороны AC={AC:.2g}")
print(f"Высота треугольника={height:.2g}")
if is_sqare == True:
    print(f"Треугольник прямоугольный")
if is_belong == True:
    print("Точка принадлежит треугольнику")
    print(f"Расстояние от точки до прямой={max_dist:.2g}")

