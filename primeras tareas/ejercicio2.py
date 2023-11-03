'''
Asier es un estudiante emprendedor de tercer año en la UAX. Tiene la teoría de que solo 
estudiar y nada de diversión acabarán por convertirlo en un trol. Para evitarlo quiere distribuir 
su tiempo disponible para ambas tareas, a lo sumo 10 horas al día en total, entre el estudio y la 
diversión. Calcula que divertirse es dos veces más interesante que estudiar, pero cree que para 
poder cumplir con las tareas diarias de la universidad la diferencia entre las horas que dedica a 
divertirse y las que dedica a estudiar debe ser a lo sumo de 1 hora. Además, debe tener en 
cuenta que sus padres le permiten dedicar como máximo 4 horas a actividades lúdicas. ¿Cómo 
debe distribuir Asier su tiempo para conseguir que sea lo más interesante posible?

'''
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