'''
Max Z = 4 x1 + 5 x2
S.a.:
2 x1 + x2 <= 8
x2 <= 5
'''
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "5+0*x"
f2 = "8-2*x"
f3 = '(30- 4*x)/3'
x = symbols('x')
plot(f1, f2, f3, (x, 0, 5))
