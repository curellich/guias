"""
¡Usted tiene la importante tarea de crear los cartones de Bingo! Para dicho propósito, se le pide que escriba
un programa con las siguientes características:
a) Los cartones están formados solamente por números enteros y positivos. No se aceptan letras ni ningún otro carácter
b) Los números posibles van del rango 00 hasta el 99 (inclusive)
c) Cada cartón consta de 5 líneas con 5 números cada línea, lo que forma un total de 25 números por carton.
Para una mejor legibilidad se pide que al imprimirlo se muestren de esa forma.
"""

from ej2.mis_funciones import generar_carton


# Funcion para imprimir los numeros en paquetes de 5
def imprimir_carton(lista_num):
    """
    :param lista_num: Es la liosta de numeros aleatorios 
    """
    contador = 0
    for i in lista_num:
        if contador % 5 == 0:  #Con esto hago el salto de linea cada 5 elementos
            print('\n')
            print(f'{i}' + '\t', end='')
        else:
            print(f'{i}' + '\t', end='')
        contador += 1
    return []


lista = generar_carton()
imprimir_carton(lista)

