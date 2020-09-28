a = float(input('Введи длину первой стороны треугольника \n'))
b = float(input('Введи длину второй стороны треугольника \n'))
c = float(input('Введи угол между этими сторонами в градусах \n'))
import math
c = math.radians(c)
cos = math.cos(c)
print ("Третья сторона равна " + str(a*b*cos))
