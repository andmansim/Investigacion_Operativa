'''
Representar gráficamente el problema y decidir en cuál de los cuatro casos nos encontramos:
• Solución única
• Solución múltiple
• Solución no acotada
• Solución no factible

Max Z = 6 x1 + 3 x2
S. a.:
2 x1 + 4 x2 <= 8
- x1 + 4 x2 <= 4
x1 - x2 <= 2
x1; x2 >= 0
'''
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
#restricciones
f1 = "(8-2*x)/4" # 2x1 + 4x2 <= 8 -- azul, para abajo
f2 = "(4+x*1)/4" # -x1 + 4x2 <= 4 --naranja, para abajo
f3 = 'x*1-2' # x1 - x2 <= 2 -- verde, para arriba
#función a maximizar
z1 = '(20-6*x)/3' # 6x1 + 3x2 = 20
z2 = '(15-6*x)/3' # 6x1 + 3x2 = 15
z3 = '(10-6*x)/3' # 6x1 + 3x2 = 10

x = symbols('x')
plot(f1, f2, f3, z1,z2, z3, (x, 0, 5))

#Es solución única, donde el punto corresponde a la recta morada que más o menos es x1=2,x2=1