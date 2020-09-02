'''
1. Escribir una función que reciba como parámetros el inicio y fin (inclusive) de un rango numérico. La función debe:
a. Imprimir en pantalla todos aquellos números que sean divisibles por 7 pero no sean divisibles por 5.
b. Imprimir el mismo resultado anterior, pero separados por coma.
Resultado Esperado: Por ejemplo, si se invoca con los parámetros 1 y 100 (puntos a y b)
      7
      14
      21
      28
      42
      49
      56
      63
      77
      84
      91
      98
7,14,21,28,42,49,56,63,77,84,91,98
'''


def funcion1(incio, fin):
    """
    Funcion que imprime por pantalla un rango de numeros divisibles por 7 y no divisibles por 5
    :param incio: Valor incial del rango
    :param fin: Valor final del rango
    :return: None
    """
    for i in range(incio, fin + 1):
        if i % 7 == 0 and i % 5 != 0:
            print(i)


def funcion2(inicio, fin):
    """
    Funcion que imprime por pantalla (separados por comas) un rango de numeros divisibles por 7 y no divisibles por 5
    :param inicio: Valor incial del rango
    :param fin: Valor final del rango
    :return: None
    """
    for i in range(inicio, fin + 1):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=', ')  # Preguntar por el operador sep


funcion1(1, 100)
funcion2(1, 100)
lista= 1,2,3,4,5
print(lista)
