from datetime import datetime
import blackjack.validaciones
from blackjack.constantes import SALDO_INCIAL

import ast

"""
Las funciones config_juego(), config_jugadore() y config_partida_inicial(), son funciones para crear la ESTRUCTURA 
DE DATOS sobre la que va a trabajar todo el programa. 
El programa va a trabajar siempre sobre un lista llamada config_partida. 
Cada elemento de la lista es un diccionario, el primer elemento de la lista siempre es la configuracion del juego
y de la banca, y dependiendo de la cantidad de jugadores, abrá 1 o más diccionarios con la configuracion / informacion 
de los jugadores.

La lista config_partida se va a guardar en un fichero. Desde donde se podrá posteriormete cargar la partida.
En el fichero la configuracion guardada contiene la configuracion del juego y jugadores, saldos y estados.

Todos los nombre de los ficheros se van a almacenar en partidas.txt, para que el usuario no necesite saber el nombre
del fichero donde se guardó la partida, sino que pueda elegirlo desde la misma.
"""


# FRONTEND (participa el usuario) *
def config_juego():
    """
    Funcion para que el usuario configure el juego, cant jugadores, barajas y modo de juego, juego de la banca.
    :return: dict con la configuracion del modo de juego.
    """
    conf_juego = {'nombre': "BANCA", 'cant_jugadores': None, 'cant_barajas': None, 'modo_juego': None,
                  'cpu': None, 'estado': None, 'saldo': 1000000, 'cartas': None}

    # Valido y asigno valores ingresados por teclado
    cant_jugadores = blackjack.validaciones.validacion_cantidad_jugadores()

    cant_barajas = blackjack.validaciones.validacion_canttidad_barajas()

    modo_juego = blackjack.validaciones.validacion_tipo_1_2()

    juego_banca = blackjack.validaciones.validacion_tipo_1_3()

    # Agrego los valores ingresados por teclado al diccionario config_juego

    conf_juego['cant_jugadores'] = cant_jugadores
    conf_juego['cant_barajas'] = cant_barajas
    if modo_juego == 1:
        conf_juego['modo_juego'] = "facil".upper()
    else:
        conf_juego['modo_juego'] = "dificil".upper()

    if juego_banca == 1:
        conf_juego['cpu'] = "arriesgado".upper()
    elif juego_banca == 2:
        conf_juego['cpu'] = "prudente".upper()
    else:
        juego_banca['cpu'] = "inteligente".upper()

    return conf_juego


# FRONTEND (participa el usuario)
def config_jugador():
    """
    Funcion donde el usuario configura a cada jugador: nombre y cpu.
    :return: dict con la configuracion del jugador
    """
    # Este es el diccionario tipo que contiene la informacion de un jugador
    conf_jugador = {'numero': None, 'nombre': input('Ingrese el nombre del jugador: ').upper(), 'cpu': None,
                    'estado': "EN JUEGO", 'saldo': SALDO_INCIAL, 'posicion': None, 'cartas': None}

    # Valido y asigno valores
    cpu = blackjack.validaciones.validacion_tipo_1_4()

    if cpu == 1:
        conf_jugador['cpu'] = "arriesgado".upper()
    elif cpu == 2:
        conf_jugador['cpu'] = "prudente".upper()
    elif cpu == 3:
        conf_jugador['cpu'] = "humano".upper()
    elif cpu == 4:
        conf_jugador['cpu'] = "inteligente".upper()

    return conf_jugador


# BACKEND
def config_partida_inicial(conf_juego):
    """
    Funcion para crear un lista con la configuracion inicial del juego, jugadores, modos, barajas, etc
    :param conf_juego: dict con la configuracion inicial del juego (USAR LA FUNCION conf_juego que crea un dict)
    :return: list con la configuracion del partida
    """
    conf_partida = []
    cant_jugadores = conf_juego['cant_jugadores']

    # La primera linea de la lista siempre es el diccionario de la configuracion del juego
    conf_partida.append(conf_juego)

    # A continuacion se agregan a la lista los diccionarios de la configuracion de cada jugador
    for i in range(1, cant_jugadores + 1):
        conf_jugadores = config_jugador()
        conf_jugadores['numero'] = i
        conf_partida.append(conf_jugadores)

    return conf_partida


# BACKEND *
def crear_archivo_partida(config_partida):
    """
    Convierte cada elemento de la lista a str y crea el archivo de la configuracion inicial de la partida
    :param config_partida: list con los elementos para guardar en el archivo. (conf_juego y conf_jugadores)
    :return: str con el nombre del archivo normalizado
    """
    # El nombre del archivo va a ser la fecha y hora normalizada
    nombre_fichero = datetime.now()
    nombre_nomalizado = ('{:%a %b %d %H:%M:%S}'.format(nombre_fichero))

    fichero = open(f"./blackjack/partidas_guardadas/{nombre_nomalizado}", 'w')

    for i in config_partida:
        fichero.write(str(i) + "\n")

    fichero.close()

    return nombre_nomalizado


# BACKEND *
def sobreescribir_archivo_partida(nombre_archivo, config_partida, lista_perdedores, lista_ganadores):
    """
    Convierte cada elemento de la lista a str y sobreescribe el archivo con la configuracion  de la partida
    :param nombre_archivo: str con el nombre del archivo a sobreescribir
    :param lista_perdedores: list con los jugadores que no tienen el saldo suficiente para jugar
    :param lista_ganadores: list con los jugadores que superaron el saldo maximo de juego
    :param config_partida: list con los elementos para guardar en el archivo. (conf_juego y conf_jugadores)
    :return: None
    """
    fichero = open(f"./blackjack/partidas_guardadas/{nombre_archivo}", 'w')

    for jugadores in config_partida:
        fichero.write(str(jugadores) + "\n")
    for ganadores in lista_ganadores:
        fichero.write(str(ganadores) + "\n")
    for perdedores in lista_perdedores:
        fichero.write(str(perdedores) + "\n")

    fichero.close()

    return


# BACKEND
def guardar_nombre_en_archivo(nombre_de_archivo):
    fichero = open("./blackjack/partidas.txt", "a")
    fichero.write(nombre_de_archivo + "\n")
    fichero.close()


# BACKEND *
def cargar_partida_de_archivo(nombre_del_archivo):
    """
    Funcion que permite utilizar la configuracion de una partida desde un archivo. Solo conf_juego y conf_jugadores
    :param nombre_del_archivo: str el nombre del archivo a cargar
    :return: list con la configuracion del juego.
    """
    nombre_del_fichero = "./blackjack/partidas_guardadas/" + nombre_del_archivo
    fichero = open(nombre_del_fichero, 'r')
    config_partida = []
    linea = fichero.readline()

    while linea != '':
        config_partida.append(ast.literal_eval(linea))
        linea = fichero.readline()

    fichero.close()

    return config_partida


# BACKEND *
def comprobacion_fichero():
    """
    Funcion para saber si existen partidas para cargar
    :return: str "VACIO" si esta vacio. Sino "CON CONTENIDO"
    """
    # compruebo si existen partidas para cargar
    fichero = open("./blackjack/partidas.txt", 'r')
    contenido = fichero.read()
    if contenido == '':
        indicador = "VACIO"
    else:
        indicador = "CON CONTENIDO"

    return indicador


# BACKEND *
def limpiar_cartas(config_partida):
    """
    Funcion que elimina todas las cartas de los jugadores
    :param config_partida: list con la configuracion inicial del juego
    :return: None
    """

    for jugadores in config_partida:
        jugadores['cartas'] = []

    return None
