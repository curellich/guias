import random


# BACKEND *
def crear_baraja_tipo():
    """
    La funcion crea la baraja francesa
    :return: list de diccionarios con las 52 cartas francesas
    """
    baraja_tipo = []  # Aqui se van a almacenar las cartas
    carta_tipo = ["valor", "palo"]  # Estas son las keys para hacer las cartas
    palos = ["pica", "diamante", "trebol", "corazones"]  # Estos son los valores para las keys 'palo'
    valores = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]  # Estos son los valores para las keys 'valor'

    for i in valores:  # Aqui se construyen las cartas y se agregan a la
        for j in palos:  # baraja_tipo
            carta = dict.fromkeys(carta_tipo)
            carta['valor'] = i
            carta['palo'] = j
            baraja_tipo.append(carta)

    return baraja_tipo


# BACKEND *
def constr_maso(num_barajas, baraja_tipo):
    """
    La funcion incrementa en n veces la cantidad de barajas dependiendo de la config del juego
    :param num_barajas: int con el numero de barajas que esta en la conf_juego
    :param baraja_tipo: list con la baraja a incrementar
    :return: list con el maso incrementado
    """
    maso = []

    # de acuerdo al num_barajas se agragan barajas_tipo a la lista maso siempre al final de la lista.
    for i in range(1, num_barajas + 1):
        maso.extend(baraja_tipo)

    return maso


# BACKEND *
def mezclar_maso(maso):
    """
    Funcion para mezclar las cartas del maso
    :param maso: list que tiene como elementos cartas en formato diccionario par(valor,palo)
    :return: None
    """
    random.shuffle(maso, random.random)


# BACKEND *
def maso_de_juego(config_partida):
    """
    Funcion que retorna un maso, mezclado con las cantidades de naipes configuradas
    :return: list maso listo para jugar
    """
    cant_barajas = config_partida[0]['cant_barajas']  # obtengo la cant de barajas de la conf
    maso = constr_maso(cant_barajas, crear_baraja_tipo())  # construyo el maso
    mezclar_maso(maso)  # mezclo el maso
    return maso


# BACKEND *
def sacar_carta(maso_mezclado):
    """
    Siempre se saca una carta de arriba del maso
    :param maso_mezclado: es el maso de juego ya barajado
    :return: dict una carta
    """
    return maso_mezclado.pop()

# BACKEND *
def maso_de_juego(conf_partida):
    """
    Este es el maso con el que se va a barajar, y se va a jugar UNA ronda
    :return: list con el maso
    """
    cant_barajas = conf_partida[0]['cant_barajas']

    # construyo el maso mezclado
    baraja_tipo = crear_baraja_tipo()
    maso_nuevo = constr_maso(cant_barajas, baraja_tipo)
    mezclar_maso(maso_nuevo)

    return maso_nuevo

# BACKEND *
def barajar(conf_partida, maso_nuevo):
    """
    Reparte dos cartas a cada jugador y a la banca, y las guarda en la conf_partida
    :param conf_partida: list con la conf_juego y conf_jugador para todos los jugadores
    :return: None
    """

    # reparto dos cartas para cada jugador y la banca
    for i in conf_partida:
        i['cartas'] = [sacar_carta(maso_nuevo), sacar_carta(maso_nuevo)]


# BACKEND *
def carta_escondida_banca(config_partida):
    """
    Funcion que quita la segunda carta de la banca
    :param config_partida: list con la configuracion del juego.
    :return: dict con la carta para retirada de las cartas de la banca
    """

    carta_escondida = config_partida[0]['cartas'].pop()

    return carta_escondida

# BACKEND *
def formato_carta(carta):
    """
    Funcion que asigna el simbolos utf-8 a cada palo de cada carta
    :param carta: dict carta con el par valor, palo
    :return: dict cons las cartas
    """
    if carta['palo'] == "pica":
        carta['palo'] = "♠"
    elif carta['palo'] == "trebol":
        carta['palo'] = "♣"
    elif carta['palo'] == "diamante":
        carta['palo'] = "♦"
    else:
        carta['palo'] = "♥"

    return carta