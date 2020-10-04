from random import randrange


def generar_carton():
    lista = []
    for i in range(0, 25):
        lista.append(randrange(0, 99 + 1, 1))
    return lista


def grabar_carton(lista_cnumeros, nombre):
    fichero = open(f'{nombre}.txt', 'w')
    contador = 0
    cadena = ""
    for i in lista_numeros:
        if contador % 5 == 0 and contador != 0:  # Con esto hago el salto de linea cada 5 elementos
            cadena = cadena + '\n'
            cadena = cadena + '\t' + ''.join(str(i))
        else:
            cadena = cadena + '\t' + ''.join(str(i))
        contador += 1
    fichero.write(cadena)
    fichero.close()

    return []
