'''
Max Z = 2x1 + x2
Con las restricciones:
x1 + x2 <= 8
3x1 + x2 <= 18
x1; x2 >= 0

Representar gráficamente y mediante un modelo de programación lineal los problemas
simétricos equivalentes en cada uno de los cuatro cuadrantes.
1 
x1 >= 0
x2 >= 0
2
x1 <= 0
x2 >= 0
3
x1 <= 0
x2 <= 0
4
x1 >= 0
x2 <= 0
'''
import sympy as sym
from sympy import symbols
from sympy.plotting import plot

x = symbols('x')

#1er cuadrante
f1 = "8-x" # x1 + x2 <= 8
f2 = "18-3*x" # 3x1 + x2 <= 18
# Max Z = 2x1 + x2
z1 = "20-2*x " 
z2 = '30-2*x'
z3 = '40-2*x'
plot(f1, f2, z1, z2, z3,(x, 0, 15), show=True, legend=True) 

#2do cuadrante
f1 = "8-x" # x1 + x2 <= 8
f2 = "18-3*x" # 3x1 + x2 <= 18
# Max Z = 2x1 + x2
z1 = "20+2*x "
z2 = '30+2*x'
z3 = '40+2*x'
plot(f1, f2, z1, z2, z3,(x, -15, 0), show=True, legend=True) 

#3er cuadrante
f1 = "8+x" # x1 + x2 <= 8
f2 = "18+3*x" # 3x1 + x2 <= 18
# Max Z = 2x1 + x2
z1 = "20+2*x "
z2 = '30+2*x'
z3 = '40+2*x'
plot(f1, f2, z1, z2, z3,(x, -15, 0), show=True, legend=True) 

#4to cuadrante
# x1 >= 0, x2 <= 0 --> reescribimos la x2: -x2 >= 0
f1 = "-8+x" # x1 + x2 <= 8
f2 = "-18+3*x" # 3x1 + x2 <= 18
# Max Z = 2x1 + x2
z1 = "-20+2*x "
z2 = '-30+2*x'
z3 = '-40+2*x'
plot(f1, f2, z1, z2, z3,(x, 0, 15), show=True, legend=True)




