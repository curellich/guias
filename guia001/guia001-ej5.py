"""
5- Realizar un programa que permita el usuario ingresar las coordenadas (x,y) de puntos del plano (se indica el fin
con el par 0,0). Luego, imprimir las coordenadas ingresadas y la distancia al origen, ordenadas de menor a mayor por
distancia. Utilizar funciones y módulos.
Tips: el modulo math contiene la función sqrt que calcula la raíz cuadradra. Para la obtención de los datos, se puede
trabajar con la función split vista anteriormente.
|𝑎, 𝑏| = '𝑎! + 𝑏!
"""
from math import sqrt


# Definicion de funciones
def distAlOrigen(coordenadas):
    par = coordenadas.split(',') #Creo la lista con elementos del string coordenadas
    x = float(par[0])
    y = float(par[1])
    distancia = float(sqrt((x ** 2) + (y ** 2)))
    return distancia


coordenadas = input('Por favor, ingrese el punto en formato x,y :')
while coordenadas != '0,0':
    print(f'La distancia al origen del punto ({coordenadas}) es: {float(distAlOrigen(coordenadas)):.2f}')
    coordenadas = input('Por favor, ingrese el punto en formato x,y :')
