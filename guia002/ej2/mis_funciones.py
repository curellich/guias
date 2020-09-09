from random import randrange


def generar_carton():
    lista = []
    for i in range(0, 25):
        lista.append(randrange(0, 99 + 1, 1))
    return lista
