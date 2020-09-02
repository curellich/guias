'''
5. Escriba una función que reciba como parámetro el radio de un circulo y devuelva una tupla conteniendo en el primer
elemento el perímetro y en el segundo el área del mismo.
TIPs: Recuerde que la fórmula del perímetro es (2 * pi * r) y el área se define como (pi * r^2). Se puede utilizar
la constante pi definida en el módulo math (import math)
Resultado Esperado: Si se utiliza la funcion con el valor de r=5, entonces debe devolver la tupla (31.415, 78.539)
'''
from math import pi


def perimetroYAreaDeUnCirculo(radio):
    perimetro = 2 * pi * radio
    area = pi * (radio ** 2)
    return perimetro, area


perimetro, area = perimetroYAreaDeUnCirculo(float(input('Dame el radio: ')))

print('El perimetro es: {0:.2f}, y el area es: {1:.2f}'.format(perimetro, area))
