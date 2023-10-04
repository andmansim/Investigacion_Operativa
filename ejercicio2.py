import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" # x1 + x2 <= 10
f2 = "1+x" # x1 -x2 <= 1
f3 = "4" # x2 <= 4
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -15, 15))

#Solución: x2 = 4, x1= 5, para mantener la diferencia de 1 entre x1 y x2