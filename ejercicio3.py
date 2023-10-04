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
f1 = "(8-2*x)/4" # 2x1 + 4x2 <= 8
f2 = "(4+x*1)/4" # -x1 + 4x2 <= 4
f3 = 'x*1-2' # x1 - x2 <= 2
#función a maximizar
z = '(20-6*x1)/3' # 6x1 + 3x2 = 20
z = '(37-6*x1)/3' # 6x1 + 3x2 = 37
z = '(30-6*x1)/3' # 6x1 + 3x2 = 30

x = symbols('x')
plot(f1, f2, f3, z, (x, -15, 15))
