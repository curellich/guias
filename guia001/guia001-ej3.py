"""
3- Crear un programa que importe el modulo creado hasta el momento (fechas) y le pida al usuario los 3 datos:
 nombre del mes, abreviatura y cantidad de días. Una vez obtenida la información por parte del usuario.
Tip: función input y analizar que tipo de variable es con type
"""

from j01.fechas import crear_mes

nombre= str(input('Ingrese el nombre del mes: '))
abreviatura=str(input('Ingrese la abreviatura: '))
dias= int(input('Ingrese la cantidad de días:'))

print(crear_mes(nombre, abreviatura, dias))


