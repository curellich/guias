"""
4. Escribir un programa que reciba como parámetro un string de elementos separados por coma y retorne una lista conte_
niendo cada elemento.
ResultadoEsperado:Siseutilizacomoparámetroelstring'14,Juana Perez,True'se espera que la función retorne la
lista ['14', 'Juana Perez', 'True']
"""


def stringALista(cadena):
    '''
    Programa que recibe una cadena separada por comas y devuelve una lista con dichos elementos
    :param cadena: Recibe un String
    :return: Una lista
    '''
    lista = cadena.split(", ")
    return lista


print(stringALista("14,Juana, true"))
