'''
Variante 4: Olvidémonos de ser un trol, no era una buena idea ¿Cuál sería la solución 
óptima del problema si el objetivo de Asier fuera divertirse lo máximo posible?
'''
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" # x1 + x2 <= 10
f2 = "1+x" # x1 -x2 <= 1
f3 = "4" # x2 <= 4
x = symbols('x')
plot(f1, f2, f3, (x, -1, 15))
#Solución: la recta comprendida entre 3 y 6 de x1, manteniendo x2 siempre 4, multiple