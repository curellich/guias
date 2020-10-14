from datetime import datetime
from blackjack.constantes import SALDO_INCIAL, CANT_MAX_JUGADORES, CANT_MAX_BARAJAS
from blackjack.cartas import barajar
from blackjack.cartas import carta_escondida_banca
from blackjack import cartas
import ast


# FRONTEND (participa el usuario)
def config_juego():
    """
    Funcion para que el usuario configure el juego, cant jugadores, barajas y modo de juego, juego de la banca.
    :return: dict con la configuracion del modo de juego.
    """
    conf_juego = {'nombre': "BANCA", 'cant_jugadores': None, 'cant_barajas': None, 'modo_juego': None,
                  'juego_banca': None, 'estado': None, 'saldo': 1000000, 'cartas': None}

    # El usuario ingresa por teclado la cantidad de jugadores
    while True:
        try:
            cant_jugadores = int(input(f'Ingrese la cantidad de jugadores (1 - {CANT_MAX_JUGADORES}): '))
            if cant_jugadores < 1 or cant_jugadores > CANT_MAX_JUGADORES:
                raise ValueError()
            break
        except:
            print(f"El numero de jugadores admitidos va desde 1 hasta {CANT_MAX_JUGADORES}")

    # El usuario ingresa por teclado la cantidad de barajas
    while True:
        try:
            cant_barajas = int(input(f'Ingrese la cantidad de barajas (1 - {CANT_MAX_BARAJAS}): '))
            if cant_barajas < 1 or cant_barajas > CANT_MAX_BARAJAS:
                raise ValueError()
            break
        except:
            print(f"El numero de barajas admitidas va desde 1 hasta {CANT_MAX_BARAJAS}")

    # El usuario ingresa el modo de juego
    while True:
        try:
            modo_juego = int(input('Ingrese el modo de juego: 1- Facil 2- Dificil: '))
            if modo_juego < 1 or modo_juego > 2:
                raise ValueError()
            break
        except:
            print('El numero debe ser "1" o "2"')

    # El usuario ingresa el juego de la banca
    while True:
        try:
            juego_banca = int(input('Ingrese el modo de juego de la banca: 1- Agresiva 2- Prudente 3- Inteligente: '))
            if juego_banca < 1 or juego_banca > 3:
                raise ValueError()
            break
        except:
            print('El numero debe ser "1" o "3"')

    # Agrego el diccionario configuracion del juego a la lista configuracion de partida
    conf_juego['cant_jugadores'] = cant_jugadores
    conf_juego['cant_barajas'] = cant_barajas
    if modo_juego == 1:
        conf_juego['modo_juego'] = "facil".upper()
    else:
        conf_juego['modo_juego'] = "dificil".upper()

    if modo_juego == 1:
        conf_juego['juego_banca'] = "arriesgado".upper()
    elif modo_juego == 2:
        conf_juego['juego_banca'] = "prudente".upper()
    else:
        conf_juego['juego_banca'] = "inteligente".upper()

    return conf_juego


# FRONTEND (participa el usuario)
def config_jugador():
    """
    Funcion donde el usuario configura a cada jugador: nombre y cpu.
    :return: dict con la configuracion del jugador
    """
    # Este es el diccionario tipo que contiene la informacion de un jugador
    conf_jugador = {'numero': None, 'nombre': None, 'cpu': None, 'estado': "EN JUEGO", 'saldo': SALDO_INCIAL,
                    'posicion': None, 'cartas': None}

    # Se ingresa el nombre del jugador
    conf_jugador['nombre'] = input('Ingrese el nombre del jugador: ').upper()

    # Se ingrese el modo de juego del jugador
    while True:
        try:
            cpu = int(
                input('Ingrese el modo de juego: 1- CPU-Arriesgado, 2- CPU-Prudente, 3- Humano, 4- Inteligente: '))
            if cpu < 1 or cpu > 4:
                raise ValueError()
            break
        except:
            print('El numero admitito va desde 1 hasta 4')

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
def config_partida_inicial(config_juego):
    """
    Funcion para crear un lista con la configuracion inicial del juego, jugadores, modos, barajas, etc
    :param config_juego: dict con la configuracion inicial del juego (USAR LA FUNCION conf_juego que crea un dict)
    :return: list con la configuracion del partida
    """
    conf_partida = []
    cant_jugadores = config_juego['cant_jugadores']

    # La primera linea de la lista siempre es el diccionario de la configuracion del juego
    conf_partida.append(config_juego)

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
    nombre_nomalizado = "%s" % nombre_fichero.isoformat()

    fichero = open(f"./blackjack/{nombre_nomalizado}", 'w')

    for i in config_partida:
        fichero.write(str(i) + "\n")

    fichero.close()

    return nombre_nomalizado


# BACKEND *
def sobreescribir_archivo_partida(nombre_archivo, config_partida):
    """
    Convierte cada elemento de la lista a str y sobreescribe el archivo con la configuracion  de la partida
    :param nombre_archivo: str con el nombre del archivo a sobreescribir
    :param config_partida: list con los elementos para guardar en el archivo. (conf_juego y conf_jugadores)
    :return: None
    """
    fichero = open(f"./blackjack/{nombre_archivo}", 'w')

    for i in config_partida:
        fichero.write(str(i) + "\n")

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
    nombre_del_fichero = "./blackjack/" + nombre_del_archivo
    fichero = open(nombre_del_fichero, 'r')
    conf_partida = []
    linea = fichero.readline()

    while linea != '':
        conf_partida.append(ast.literal_eval(linea))
        linea = fichero.readline()

    fichero.close()

    return conf_partida


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
