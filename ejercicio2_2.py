'''
Variante 2: Si ahora eliminamos la restricción de que el número máximo de horas 
disponibles es de 10 horas ¿cuál sería la solución óptima del problema?
'''

import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "1+x" # x1 -x2 <= 1
f2 = "4" # x2 <= 4
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, Z1, Z2, Z3, (x, -1, 15))
#La solución no está acotada al no tener horas máximas de estudio, como mucho podríamos interpretar como las horas maximas 24h que es lo que dura un día. 