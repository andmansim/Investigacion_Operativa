'''
Variante 1: Supongamos ahora que Asier valora exactamente igual las horas dedicadas 
a estudiar que las dedicadas a divertirse. ¿Cuál sería ahora la solución óptima?

'''
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
#unica
#Solución: x2 = 4, x1= 5, para mantener la diferencia de 1 entre x1 y x2