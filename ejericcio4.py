'''
Enunciado:
La industria de juguetes “Galaxia” produce dos tipos de juguetes:
    • Space Ray --> x1
    • Zapper --> x2
Los recursos están limitados a:
    • 1200 kg de plástico por semana
    • 40 horas de producción semanal
Los requerimientos de Marketing son:
    • La producción total no puede exceder de 800 docenas. --> x1 + x2 <= 800
    • El número de docenas de Space Rays no puede exceder al número de docenas de  
      Zappers por más de 450. --> x1 - x2 <= 450
Los requerimientos Tecnológicos son:
    • Space Rays requiere 2 kg de plástico y 3 minutos de producción por docena. --> 2/3 1 docena = x1
    • Zappers requiere 1 kg de plástico y 4 minutos de producción por docena.---> 1/4 1 docena = x2
El plan de producción actual se establece mediante los siguientes criterios:
    • Fabricar la mayor cantidad del producto que deje más beneficios, el cual corresponde 
      a Space Ray (8 € de utilidad por docena). --> 8 x1 
    • Usar la menor cantidad de recursos para producir Zappers, porque estos dejan una 
      menor utilidad (5 € de utilidad por docena). --> 5 x2

Se pide:
a) Emplear el método gráfico para visualizar las restricciones. Calcular Z, x1 y x2 para el 
plan de producción actual. (3 puntos)
b) ¿Se puede hacer mejor? ¿Cómo? (4 puntos)
c) Calcular Z, x1 y x2 para el mejor plan de producción sin Zapper (1 punto)
d) Calcular Z, x1 y x2 para el mejor plan de producción sin Space Ray (1 punto)


Solución:
El plan de producción actual es, por tanto:
    • Space Rays = 550 docenas --> 1 x1 = 550
    • Zappers = 100 docenas --> 1 x2 = 100
Obteniéndose una utilidad Z de 4.900 € por semana.
Las variables de decisión son:
    • x1 = Producción de Space Rays (en docenas por semana)
    • x2 = Producción de Zappers (en docenas por semana)

Plático: 2 x1 + x2 <= 1200
Horas: 3 x1 + 4 x2 <= 2400
Restricciones: x1 + x2 <= 800, x1 - x2 <= 450
Dinero a maximizar: 8 x1 + 5 x2 = 4900 --> Z = 4900



'''