import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #x2 + x1 <= 10
f2 = "1+x" #x1 -x2 <= 1
f3 = "4" #x2 <= 4
Z1 = "16-x"
Z2 = "14-x"
Z3 = "13-x"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -1, 15))
#El area optima es la parte de abajo de la naranja, la azul y la verde --> colorear en un pdf
#Solución: x2 = 4, x1= 5, para mantener la diferencia de 1 entre x1 y x2