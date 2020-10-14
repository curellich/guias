from datetime import datetime
from random import randrange

def numero_aleatorio():
   numero = randrange(0,9999999999,1)
   return numero

def requerimiento_1():
    fichero = open('envios.txt','r')
    ficheroNuevo = open('menos.txt','w')
    lista=[] #Aqui se van a almacenar como elementos las lineas del fichero
    cadena ="" #Aqui se va a guardar toda la cadena que se va a guardar despues en el ficheroNuevo
    linea = fichero.readline()

    while linea != '':
        lista = linea.split(sep='-')
        if int(lista[0]) < 50000:
            cadena = cadena + ' ' + lista[0] + ' ' + lista[1]
            cadena += '\n'
        linea = fichero.readline()

    ficheroNuevo.write(cadena)
    ficheroNuevo.close()
    fichero.close()
    return []

def requerimiento_2():
    fichero = open('envios.txt', 'r')
    ficheroNuevo = open('internacionales.txt', 'w')
    lista = []  # Aqui se van a almacenar como elementos las lineas del fichero
    cadena = ""  # Aqui se va a guardar toda la cadena que se va a guardar despues en el ficheroNuevo
    linea = fichero.readline()

    while linea != '':
        lista = linea.split(sep='-')
        if lista[3] != 'AR':
            cadena = cadena + linea
            cadena += '\n'
        linea = fichero.readline()

    ficheroNuevo.write(cadena)
    ficheroNuevo.close()
    fichero.close()
    return []

def requerimiento_3():
    fichero = open('envios.txt', 'r')
    ficheroNuevo = open('con_iva.txt', 'w')
    lista = []  # Aqui se van a almacenar como elementos las lineas del fichero
    cadena = ""  # Aqui se va a guardar toda la cadena que se va a guardar despues en el ficheroNuevo
    linea = fichero.readline()


    while linea != '':
        lista = linea.split(sep='-')
        lista[6]= float(lista[6])+ round(float(lista[6])*0.21)  # a cada precio le sumo el 21%
        cadena = cadena + ' ' + lista[1] +' peso ' + lista[7]+ ' precio ' + str(lista[6])
        cadena += '\n'
        linea = fichero.readline()

    ficheroNuevo.write(cadena)
    ficheroNuevo.close()
    fichero.close()
    return []

def requerimiento_4():
    fichero = open('envios.txt', 'r')
    ficheroNuevo = open('procesados.txt', 'w')
    lista = []  # Aqui se van a almacenar como elementos las lineas del fichero
    cadena = ""  # Aqui se va a guardar toda la cadena que se va a guardar despues en el ficheroNuevo
    linea = fichero.readline()
    ahora = str(datetime.now())


    while linea != '':
        lista = linea.split(sep='-')
        if lista[8] == False:
            cadena = cadena + ' ' + lista[0] + ' ' + lista[1].upper() + ' precio ' + ahora + '' + str(
                numero_aleatorio()) + ' ' + lista[6]
        else:
            cadena = cadena + ' ' + lista[0] +' ' + lista[1].upper()+ ' precio ' + ahora + '' + str(numero_aleatorio())
        cadena += '\n'
        linea = fichero.readline()

    ficheroNuevo.write(cadena)
    ficheroNuevo.close()
    fichero.close()

    return []


requerimiento_1()
requerimiento_2()
requerimiento_3()
requerimiento_4()