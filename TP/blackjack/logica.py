from random import randint
from blackjack.constantes import SALDO_GANADOR


# BACKEND *
def suma_cartas(jugador):
    """
    Funcion que suma las cartas del usuario o maquina
    :param jugador: dict con las informacion del jugador
    :return: int con la suma de las cartas
    """
    suma_cartas_numericas = 0
    suma_cartas_de_la_corte = 0
    suma_total = 0
    cartas_numericas = []
    cartas_de_la_corte = []
    cartas_as = []

    # separo las cartas numericas, de las cartas de la corte y de los As
    for carta in jugador['cartas']:
        if str(carta['valor']).isdigit():
            cartas_numericas.append(carta['valor'])
        elif str(carta['valor']).isalpha() == True and carta['valor'] != "A":
            cartas_de_la_corte.append(carta['valor'])
        elif str(carta['valor']).isalpha() == True and carta['valor'] == "A":
            cartas_as.append(carta['valor'])

    # Primero sumos las cartas numericas
    if len(cartas_numericas) != 0:
        for carta_num in cartas_numericas:
            suma_cartas_numericas = suma_cartas_numericas + carta_num

    # Segundo sumo las carta de la corte
    if len(cartas_de_la_corte) != 0:
        for carta_corte in cartas_de_la_corte:
            suma_cartas_de_la_corte = suma_cartas_de_la_corte + 10

    # Sumo cartas numericas y de la corte
    suma_total = suma_cartas_numericas + suma_cartas_de_la_corte
    if suma_total > 21:
        return suma_total

    # Suma todas las cartas "As" intentando no pasarse de 21
    if suma_total == 21 and len(cartas_as) != 0:
        for carta in cartas_as:
            suma_total = suma_total + 1
        return suma_total  # se pasa de 21 pero las suma igual con valor de 1 cada as

    elif suma_total < 21 and len(cartas_as) > 1:
        while len(cartas_as) != 1:
            suma_total = suma_total + 1
            cartas_as.pop()
        if suma_total > 21:
            return suma_total + 1  # se pasa y devuelve el valor habiendo sumado todos los as con valor 1
        elif suma_total < 21 and suma_total + 11 <= 21:
            suma_total = suma_total + 11
            return suma_total
        else:
            suma_total = suma_total + 1
            return suma_total
    elif suma_total < 21 and len(cartas_as) == 1:
        if suma_total + 11 <= 21:
            suma_total = suma_total + 11
            return suma_total
        else:
            suma_total = suma_total + 1
            return suma_total

    return suma_total


# BACKEND *
def cpu_arriesgado(nombre_jugador, config_partida):  # analiza pedir cartas si su valor no está entre 17-21.
    """
    Funcion para que el cpu_arriesgado decida pedir carta o no.
    :param nombre_jugador: str con el nombre del jugador
    :param config_partida: list con la configuracion del juego
    :return: str con "PEDIR CARTA" o "PLANTARME"
    """
    jugador = {}
    for jugadores in config_partida:
        if nombre_jugador == jugadores['nombre']:
            jugador = jugadores

    cartas = suma_cartas(jugador)

    # Mientras las cartas del jugador sean perdedoras
    # Solicita cartas hasta sus cartas sean ganadoras, igualar 21 o pasarse.
    while cartas < mayor_suma(config_partida) and cartas != 21 and cartas < 21:
        return "PEDIR CARTA"

    # Si sus cartas son hasta ahora ganadoras juega arriesgado
    if cartas < 18 and cartas != 21:
        return "PEDIR CARTA"
    else:
        return "PLANTARME"


# BACKEND *
def cpu_prudente(nombre_jugador, config_partida):
    """
    Funcion para que el cpu_prudente decida pedir carta o no, si sus cartas son menores a 14 tira la moneda.
    :param nombre_jugador: str con el nombre del jugador
    :param config_partida: list con la configuracion del juego
    :return: str con "PEDIR CARTA" o "PLANTARME"
    """
    jugador = {}
    for jugadores in config_partida:
        if nombre_jugador == jugadores['nombre']:
            jugador = jugadores

    cartas = suma_cartas(jugador)
    # Mientras las cartas del jugador sean perdedoras
    # Solicita cartas hasta sus cartas sean ganadoras, igualar 21 o pasarse.

    while cartas < mayor_suma(config_partida) and cartas != 21 and cartas < 21:
        return "PEDIR CARTA"

    # Si las cartas del jugador son hasta ahora ganadoras juega prudente
    if cartas < 14 and cartas != 21:
        desicion = flip_coin()
        return desicion
    else:
        return "PLANTARME"


# BACKEND *
def flip_coin():
    """
    Funcion que genera una decision aleatoria.
    :return: str "PEDIR CARTA" o "PLANTARME"
    """
    numero = randint(0, 1)
    if numero == 1:
        desicion = "PEDIR CARTA"
    else:
        desicion = "PLANTARME"
    return desicion


# BACKEND *
def cpu_inteligente(nombre_jugador, config_partida):  # analiza los otros jugadores y decide si jugar
    """
    Funcion para que el cpu_inteligencia_artifical decida pedir carta o no, despues de analizar los otros jugadores
    :param nombre_jugador: str con el nombre del jugador
    :param config_partida: list con la configuracion del juego
    :return: str con "PEDIR CARTA" o "PLANTARME"
    """
    jugador = {}  # este es el jugador actual
    for jugadores in config_partida:
        if nombre_jugador == jugadores['nombre']:
            jugador = jugadores

    mayor_puntaje = mayor_suma(config_partida)  # el mayor puntaje de las cartas ganadoras en la mesa
    cartas = suma_cartas(jugador)  # el puntaje de las cartas del jugador actual

    if cartas < mayor_puntaje:
        return "PEDIR CARTA"
    else:
        return "PLANTARME"


# BACKEND *
def mayor_suma(config_partida):
    """
    Funcion para calcular el total de las cartas ganadoras hasta el momento
    :param config_partida: list con la configuracion del juego
    :return: int con el total
    """
    mayor = 0  # siempre es la banca

    for jugadores in config_partida:
        suma = suma_cartas(jugadores)
        if mayor < suma and suma < 22:
            mayor = suma

    return mayor


# BACKEND *
def actualizacion_estados(config_partida):
    """
    Funcion que analiza las cartas de los jugadores y actualiza su estado
    :param config_partida: list con la configuracion del juego
    :return: None
    """
    # el jugador que tiene suma de cartas mas altas validas recibe el estado de GANA
    # el resto recibe el estado PIERDE
    # si hay empate los que tienen la suma de cartas mas altas validas reciben el estado de GANA
    mayor = mayor_suma(config_partida)
    ganadores = []

    for jugadores in config_partida:
        if suma_cartas(jugadores) == mayor:
            ganadores.append(jugadores['nombre'])

    if "BANCA" in ganadores and len(ganadores) != 1:
        if config_partida[0]['modo_juego'] == "FACIL":
            ganadores.remove("BANCA")

    for jugadores in config_partida:
        if jugadores['nombre'] in ganadores:
            jugadores['estado'] = "GANA"
        else:
            jugadores['estado'] = "PIERDE"
    return


# BACKEND *
def actualizacion_saldos(config_partida):
    """
    Funcion que actualiza saldos a ganadores y perdedores
    :param config_partida: list configuracion del juego
    :return: None
    """
    pozo = 0
    numero_ganadores = 0
    for jugadores in config_partida:
        jugadores['saldo'] = jugadores['saldo'] - 200
        pozo = pozo + 200
        if jugadores['estado'] == "GANA":
            numero_ganadores = numero_ganadores + 1

    try:
        premio = pozo / numero_ganadores
    except:
        premio = 0

    for jugadores in config_partida:
        if jugadores['estado'] == "GANA":
            jugadores['saldo'] = jugadores['saldo'] + premio

    return


# BACKEND *
def analisis_continuidad_jugador(jugador):
    """
    Funcion que analiza si el jugador puede seguir o quedó fuera de juego.
    :param jugador: dict con la informacion del jugador
    :return: str "EN JUEGO" o "FUERA DE JUEGO"
    """

    if jugador['saldo'] < 200:
        analisis = "FUERA DE JUEGO"
    else:
        analisis = "EN JUEGO"

    return analisis


# BACKEND *
def eliminacion_perdedores(config_partida):
    """
    Funcion que quita los jugadores cuyo estado es "FUERA DE JUEGO" y los guarda en una lista.
    :param config_partida: list con la configuracion del juego
    :return: list con todos los perdedores
    """
    lista_perdedores = []

    for jugadores in config_partida:
        if analisis_continuidad_jugador(jugadores) == "FUERA DE JUEGO":
            jugadores['estado'] = "FUERA DE JUEGO"
            lista_perdedores.append(jugadores.copy())

        else:
            jugadores['estado'] = "EN JUEGO"

    for perdedores in lista_perdedores:
        if perdedores in config_partida:
            config_partida.remove(perdedores)

    return list(lista_perdedores)


# BACKEND *
def analisis_continuidad_juego(config_partida):
    """
    Funcion que decide si finaliza el juego o permite al jugador continuar
    :param config_partida: list con la configuracion del juego
    :return: str "FIN DE JUEGO" o "PUEDE CONTINUAR"
    """
    # Averiguo si solo queda la banca porque el resto tiene saldo cero
    if len(config_partida) == 1:
        return "FIN DE JUEGO"
    # si algun/os jugador supero o igualo el saldo ganador
    else:
        for jugadores in config_partida:
            if jugadores['nombre'] == "BANCA":
                continue
            else:
                if jugadores['saldo'] >= SALDO_GANADOR:
                    return "FIN DE JUEGO"

    # si nada de lo anterior sucedió
    return "PUEDE CONTINUAR"


# BACKEND *
def pause():
    """
    Funcion que solo sirve para hacer una pausa y que el usuario aprete cualquier tecla para continuar
    :return:
    """
    input()
