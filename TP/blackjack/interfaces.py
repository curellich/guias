from blackjack.cartas import sacar_carta
from blackjack.logica import suma_cartas
from blackjack.logica import cpu_arriesgado
from blackjack.logica import cpu_prudente
from blackjack.logica import cpu_inteligente
from blackjack.cartas import formato_carta
from blackjack.logica import analisis_continuidad_juego
from blackjack.configuracion import comprobacion_fichero
from blackjack.constantes import SALDO_GANADOR


# BACKEND *
def cartel_bienvenida():
    """
    Funcion que imprime el encabezado del juego
    :return:
    """
    print(f'{"*" * 90:^90}')
    print('\x1b[0;30;47m' + f'{"BIENVENIDO AL BLACK JACK":^90}' + '\x1b[0m')
    print(f'{"*" * 90:^90}')

    return None


# BACKEND *
def cartel_configuracion_juego():
    """
    Funcion que imprime el encabezado del juego
    :return:
    """
    print(f'{"*" * 90:^90}')
    print('\x1b[0;30;47m' + f'{"CONFIGURACION DEL JUEGO":^90}' + '\x1b[0m')
    print(f'{"*" * 90:^90}')
    return None


# BACKEND *
def cartel_cartas_en_la_mesa():
    """
    Funcion que imprime el encabezado del juego
    :return:
    """
    print(f'{"*" * 90:^90}')
    print('\x1b[0;30;47m' + f'{"CARTAS EN LA MESA":^90}' + '\x1b[0m')
    print(f'{"*" * 90:^90}')
    return None


# FRONTEND *
def menu_inicial():
    """
    Funcion que muestra un menu y permite decidir si se inicia un juego nuevo o se carga una partida
    Emplea el metodo comprobacion_de_fichero para saber si partidas.txt tiene alguna partida para ser cargada
    :return: int con la opcion seleccionada
    """
    indicador = comprobacion_fichero()

    # no existen partidas grabadas
    if indicador == "VACIO":
        print("No existen partidas anteriores!!! \n")
        resultado = "Juego Nuevo"

    # si existe partidas grabadas
    else:
        print("Seleccione la opcion deseada: ")
        print("""
                \x1b[0;31;23m 1-\x1b[0m Cargar Partida
                \x1b[0;31;23m 2-\x1b[0m Juego Nuevo
                """)

        # Valida el ingreso por teclado
        while True:
            try:
                opcion = int(input('Opción ' + '\x1b[0;31;23m' + '(1-2)' + '\x1b[0m' + ': '))

                if opcion != 1 and opcion != 2:
                    raise ValueError
                break
            except:
                print(f"La opción no es válida. Intente nuevamente")

        # Modifico la variable resultado para ser retornada
        if opcion == 1:
            resultado = "Cargar Partida"
        else:
            resultado = "Juego Nuevo"

    return resultado


# FRONTEND

def menu_cargar_partida():
    """
    Función que permite extraer el nombre del fichero desde partidas.txt para cargar la partida
    :return: str con el nombre del archivo
    """
    # Creo una lista con las partidas guardas
    fichero = open("./blackjack/partidas.txt", "r")
    lista = fichero.readlines()
    fichero.close()

    print("Las partidas guardadas son:")

    # El contador es usado para numerar las partidas al momento de imprimirlas por pantalla y que permita al usuario
    # elegir una opción despues

    contador = 0
    for partida in lista:
        print('\x1b[0;31;23m' + f'{contador + 1}-', partida + '\x1b[0m')
        contador = contador + 1
    print("\n")

    # Valido el ingreso por teclado
    while True:
        try:
            opcion = int(input(f'Seleccione la partida a cargar:' '\x1b[0;31;23m' + f'(1-{contador}): ' + '\x1b[0m'))

            if opcion < 1 or opcion > contador:
                raise ValueError
            break
        except:
            print(f"La opción no es válida. Intente nuevamente")

    # Guardo el nombre del archivo como un str en la variable y elimino caracteres especiales del extremo derecho
    nombre_fichero = str(lista[opcion - 1]).rstrip()

    return nombre_fichero


# FRONTEND *
def menu_jugador_humano():
    """
    Funcion que muestra el menu de juego al jugador.
    :return: Opcion
    """

    print("""
    \x1b[0;31;23m 1-\x1b[0m Pedir carta
    \x1b[0;31;23m 2-\x1b[0m Plantarme 
    """)

    # Valido el ingreso por teclado
    while True:
        try:
            opcion = int(input('Opción ' + '\x1b[0;31;23m' + '(1-2)' + '\x1b[0m' + ': '))

            if opcion != 1 and opcion != 2:
                raise ValueError
            break
        except:
            print(f"La opción no es válida. Intente nuevamente")

    # Modifico la variable opcion para ser retornada de acuerdo a la opcion elegida por el usuario
    if opcion == 1:
        opcion = "PEDIR CARTA"
    else:
        opcion = "PLANTARME"

    return opcion


# FRONTEND *
def mostrar_cartas_mesa(config_partida):
    """
    Funcion que muestra las cartas que estan jugadas en la mesa (es decir que estan en la conf_partida)
    :param config_partida: list con la configuracion de la partida
    :return: None
    """

    # Busco dentro de la estructura de datos del juego las cartas de cada jugador, cada carta va a usar la funcion
    # formato_carta para mostrar el valor y el palo de la carta
    for i in config_partida:
        cartas = i['cartas']
        cartas_formateadas = []
        for j in cartas:
            cartas_formateadas.append(formato_carta(j))
        print(f"{i['nombre']}", end=' ')
        for k in cartas_formateadas:
            print(f"{k['valor']}{k['palo']}", end=' ')
        print("\n")
    return None


# FRONTEND  *
def mostrar_cartas_jugada(nombre_jugador, config_partida):
    """
    Funcion que imprime por pantalla las cartas de un jugador, ya sea humano o maquina. Esto ya es durante la ronda
    :param nombre_jugador: str con el nombre
    :param config_partida: list con la configuracion de la partida
    :return: None
    """
    cartas = []
    cartas_formateadas = []

    for jugador in config_partida:
        if jugador['nombre'] == nombre_jugador:
            cartas = jugador['cartas']

    for i in cartas:
        cartas_formateadas.append(formato_carta(i))

    for i in cartas_formateadas:
        print(f"{str(i['valor'])}{i['palo']}", end=' ')

    return


# FRONTEND *
def jugada_humano(nombre_jugador, config_partida, maso):
    """
    Funcion que desarrolla la jugada de un jugador humano, las cartas recibidas se agregan a la config_partida
    :param nombre_jugador: str con el nombre del jugador
    :param config_partida: list con la configuracion del juego
    :param maso: list con las cartas que se estan jugando
    :return:
    """
    # con el nombre del jugador busco el dict que corresponde al jugador y lo asigno
    jugador = {}
    for jugadores in config_partida:
        if nombre_jugador == jugadores['nombre']:
            jugador = jugadores
            break

    print('\x1b[0;30;47m' + f'Turno : {nombre_jugador}' + '\x1b[0m', end=' --> Cartas: ')

    # muestro las cartas del jugador
    mostrar_cartas_jugada(nombre_jugador, config_partida)

    # Muestro por pantalla si el jugador gana o pierde
    mostrar_blackjack_o_se_paso(jugador)

    if suma_cartas(jugador) < 21:

        # muestro las opciones de juego
        opcion = str(menu_jugador_humano())  # se muestran las opciones jugar o plantarse

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)  # se muestran las cartas agregadas

            # Muestro por pantalla si el jugador gana o pierde
            mostrar_blackjack_o_se_paso(jugador)

        while opcion != "PLANTARME" and suma_cartas(jugador) < 21:  #
            opcion = menu_jugador_humano()
            if opcion == "PLANTARME":
                print("\n")
                break
            carta = sacar_carta(maso)
            jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            # Muestro por pantalla si el jugador gana o pierde
            mostrar_blackjack_o_se_paso(jugador)

    return


# FRONTEND *
def mostrar_jugada_cpu(nombre_jugador, config_partida, maso):
    """
        Funcion que desarrolla la jugada de un jugador cpu, las cartas recibidas se agregan a la config_juego
        :param nombre_jugador: str con el nombre del jugador
        :param config_partida: list con la configuracion del juego
        :param maso: list con las cartas del maso que se están jugando
        :return:
        """
    # con el nombre del jugador busco el dict que corresponde al jugador y lo asigno
    jugador = {}
    for jugadores in config_partida:
        if nombre_jugador == jugadores['nombre']:
            jugador = jugadores

    print('\x1b[0;30;47m' + f'Turno : {nombre_jugador}' + '\x1b[0m' + f" ({jugador['cpu']})", end=' --> Cartas: ')

    # muestro las cartas del jugador
    mostrar_cartas_jugada(nombre_jugador, config_partida)

    # Muestro por pantalla si el jugador gana o pierde
    mostrar_blackjack_o_se_paso(jugador)

    # DESARROLLO DEL JUEGO PARA EL CPU ARRIESGADO
    if jugador['cpu'] == 'ARRIESGADO':
        opcion = cpu_arriesgado(jugador['nombre'], config_partida)
        print('\nCPU decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            # Muestro por pantalla si el jugador gana o pierde
            if suma_cartas(jugador) == 21:
                print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
            elif suma_cartas(jugador) > 21:
                print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_arriesgado(jugador['nombre'], config_partida)
                print('\nCPU decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)
                # Muetro por pantalla si el jugador gana o pierde
                if suma_cartas(jugador) == 21:
                    print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
                elif suma_cartas(jugador) > 21:
                    print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

    # DESARROLLO DEL JUEGO PARA CPU PRUDENTE
    elif jugador['cpu'] == 'PRUDENTE':
        opcion = cpu_prudente(jugador['nombre'], config_partida)
        print('\nCPU decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            # Muestro por pantalla si el jugador gana o pierde
            if suma_cartas(jugador) == 21:
                print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
            elif suma_cartas(jugador) > 21:
                print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_prudente(jugador['nombre'], config_partida)
                print('\nCPU decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)
                # Muestro por pantalla si el jugador gana o pierde
                if suma_cartas(jugador) == 21:
                    print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
                elif suma_cartas(jugador) > 21:
                    print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

    # DESARROLLO DEL JUEGO PARA CPU INTELIGENTE
    elif jugador['cpu'] == 'INTELIGENTE':
        opcion = cpu_inteligente(jugador['nombre'], config_partida)
        print('\nCPU decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            # Muestro por pantalla si el jugador gana o pierde
            if suma_cartas(jugador) == 21:
                print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
            elif suma_cartas(jugador) > 21:
                print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_inteligente(jugador['nombre'], config_partida)
                print('\nCPU decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)
                # Muestro por pantalla si el jugador gana o pierde
                if suma_cartas(jugador) == 21:
                    print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
                elif suma_cartas(jugador) > 21:
                    print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

    return


# FRONTEND *
def mostrar_jugada_banca(nombre_jugador, config_partida, maso):
    """
        Funcion que desarrolla la jugada de la banca, las cartas recibidas se agregan a la config_juego
        :param nombre_jugador: str con el nombre del jugador
        :param config_partida: list con la configuracion del juego
        :param maso: list con las cartas del maso que se están jugando
        :return:
        """
    jugador = {}
    for jugadores in config_partida:
        if nombre_jugador == jugadores['nombre']:
            jugador = jugadores

    print('\x1b[0;30;47m' + f'Turno : {nombre_jugador}' + '\x1b[0m' + f"({jugador['juego_banca']})",
          end=' --> Cartas: ')
    # muestro las cartas del jugador
    mostrar_cartas_jugada(nombre_jugador, config_partida)

    # Muestro por pantalla si la banca gana o pierde
    mostrar_blackjack_o_se_paso(jugador)

    # DESARROLLO DEL JUEGO PARA EL BANCA ARRIESGADO
    if jugador['juego_banca'] == 'ARRIESGADO':
        opcion = cpu_arriesgado(jugador['nombre'], config_partida)
        print('\nCPU decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            # Muestro por pantalla si la banca gana o pierde
            if suma_cartas(jugador) == 21:
                print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
            elif suma_cartas(jugador) > 21:
                print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_arriesgado(jugador['nombre'], config_partida)
                print('\nBANCA decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)
                # Muestro por pantalla si la banca gana o pierde
                if suma_cartas(jugador) == 21:
                    print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
                elif suma_cartas(jugador) > 21:
                    print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

    # DESARROLLO DEL JUEGO PARA BANCA PRUDENTE
    elif jugador['juego_banca'] == 'PRUDENTE':
        opcion = cpu_prudente(jugador['nombre'], config_partida)
        print('\nBANCA decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            # Muestro por pantalla si la banca gana o pierde
            if suma_cartas(jugador) == 21:
                print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
            elif suma_cartas(jugador) > 21:
                print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_prudente(jugador['nombre'], config_partida)
                print('\nBANCA decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)

                # Muestro por pantalla si la banca gana o pierde
                if suma_cartas(jugador) == 21:
                    print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
                elif suma_cartas(jugador) > 21:
                    print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

    # DESARROLLO DEL JUEGO PARA BANCA INTELIGENTE
    elif jugador['juego_banca'] == 'INTELIGENTE':
        opcion = cpu_inteligente(jugador['nombre'], config_partida)
        print('\nBANCA decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            # Muestro por pantalla si la banca gana o pierde
            if suma_cartas(jugador) == 21:
                print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
            elif suma_cartas(jugador) > 21:
                print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_inteligente(jugador['nombre'], config_partida)
                print('\nBANCA decide--> ' + '\x1b[0;33;33m' + f'{opcion}' + '\x1b[0m')
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)

                # Muestro por pantalla si la banca gana o pierde
                if suma_cartas(jugador) == 21:
                    print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
                elif suma_cartas(jugador) > 21:
                    print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

    return


# BACKEND
def mostrar_blackjack_o_se_paso(jugador):
    """
    Funcion que muestra por pantalla si el jugador durante su turno hizo blackjack o perdió
    :param jugador: dict con la informacion del jugador
    :return: None
    """

    if suma_cartas(jugador) == 21:
        print('\x1b[0;32;25m' + "¡¡¡BLACKJACK!!!" + '\x1b[0m')
    elif suma_cartas(jugador) > 21:
        print('\x1b[0;32;25m' + "--->MAYOR A 21 :(" + '\x1b[0m')

    return None


# FRONTEND *
def mostrar_ganadores_ronda(config_partida):
    """
    Funcion que imprime por pantalla el/los jugadores ganadores que reciben premio
    :param config_partida: list con la configuracion del juego
    :return: None
    """
    ganadores = 0
    for jugadores in config_partida:
        if jugadores['estado'] == "GANA":
            ganadores = ganadores + 1
            print(f"{'*' * 90:^90}")
            print('\x1b[5;37;41m' + f"{jugadores['nombre'] + ' ¡¡¡GANA!!!':^90}" + '\x1b[0m')
            print(f"{'*' * 90:^90}")

    if ganadores == 0:
        print(f"{'*' * 90:^90}")
        print('\x1b[5;37;41m' + f"{'¡¡¡ NADIE-GANA!!!':^90}" + '\x1b[0m')
        print(f"{'*' * 90:^90}")


# FRONTEND *
def mostrar_tabla(config_partida, lista_perdedores, lista_ganadores):
    """
    Funcion que muestra jugadores, saldos y estados. Ordenados por saldo
    :param lista_perdedores: list con los jugadores que no tienen saldo para seguir jugando
    :param config_partida: list con la config_partida
    :return:
    """
    cabecera = ('JUGADOR', 'SALDO', 'ESTADO')
    print(f'{"*" * 90:^90}')
    print('\x1b[0;30;47m' + f'{"TABLA DE SALDOS Y ESTADOS DEL JUEGO":^90}' + '\x1b[0m')
    print(f'{"*" * 90:^90}')

    # imprimo la cabecera de la tabla
    print('\x1b[0;36;33m' + f'|{"-" * 18:^27} |', f'{"-" * 18:^27} |', f'{"-" * 18:^27} |' + '\x1b[0m')
    print('\x1b[0;36;33m' + f'|{cabecera[0]:^27} |', f'{cabecera[1]:^27} |', f'{cabecera[2]:^27} |' + '\x1b[0m')
    print('\x1b[0;36;33m' + f'|{"-" * 18:^27} |', f'{"-" * 18:^27} |', f'{"-" * 18:^27} |' + '\x1b[0m')

    # imprimo los datos de los jugadores que tienen saldo ganador
    if len(lista_ganadores) != 0:
        print('\x1b[0;36;33m' + f'|{"-" * 18:^27} |', f'{"-" * 18:^27} |', f'{"-" * 18:^27} |' + '\x1b[0m')
        for ganadores in lista_ganadores:
            print('\x1b[0;36;25m' + f"|{ganadores['nombre']:^27} |", f"{int(ganadores['saldo']):^27} |",
                  f"{ganadores['estado']:^27} |" + '\x1b[0m')
        print('\x1b[0;36;33m' + f'|{"_" * 18:^27} |', f'{"_" * 18:^27} |', f'{"_" * 18:^27} |' + '\x1b[0m')

    # imprimo los datos de cada jugador en juego
    for jugadores in config_partida:
        if jugadores['nombre'] == "BANCA":
            continue
        else:
            print('\x1b[0;36;33m' + f"|{jugadores['nombre']:^27} |", f"{int(jugadores['saldo']):^27} |",
                  f"{jugadores['estado']:^27} |" + '\x1b[0m')

    # imprimo los datos de los jugadores que estan fuera de juego
    if len(lista_perdedores) != 0:
        print('\x1b[0;36;33m' + f'|{"-" * 18:^27} |', f'{"-" * 18:^27} |', f'{"-" * 18:^27} |' + '\x1b[0m')
        for perdedores in lista_perdedores:
            print('\x1b[0;37;31m' + f"|{perdedores['nombre']:^27} |", f"{int(perdedores['saldo']):^27} |",
                  f"{perdedores['estado']:^27} |" + '\x1b[0m')
    print('\x1b[0;36;33m' + f'|{"_" * 18:^27} |', f'{"_" * 18:^27} |', f'{"_" * 18:^27} |' + '\x1b[0m')

    return None


# FRONTEND
def mostrar_ganador_juego(config_partida):
    """
    Funcion que busca en la canfig_partida el jugador que igualo o supero el saldo ganador y lo muestra en pantalla
    :param config_partida:
    :return: None
    """
    lista_ganadores = []
    for jugadores in config_partida:
        if jugadores['nombre'] != 'BANCA' and jugadores['saldo'] >= SALDO_GANADOR:
            lista_ganadores.append(jugadores)

    if len(lista_ganadores) != 0:
        for ganadores in lista_ganadores:
            print(f"{'*' * 90:^90}")
            print('\x1b[5;31;46m' + f"{'GANADOR/ES DEL JUEGO: ' + ganadores['nombre']:^90}" + '\x1b[0m')
            print(f"{'*' * 90:^90}")

        print("Fin del juego")


# FRONTEND *
def cierre_juego(config_partida, lista_ganadores):
    """
    Funcion  para que el usuario decida continuar o no.
    :return: "FINALIZAR" o "CONTINUAR"
    """

    opcion = ""
    if analisis_continuidad_juego(config_partida, lista_ganadores) == "PUEDE CONTINUAR":
        print("-" * 3,
              "Presione " + '\x1b[0;31;23m' + '1' + '\x1b[0m' + ' para CONTINUAR o ' +
              '\x1b[0;31;23m' + '2' + '\x1b[0m' + ' para FINALIZAR el juego',
              "-" * 3)

        while True:
            try:
                opcion = int(input('Opción ' + '\x1b[0;31;23m' + '(1-2)' + '\x1b[0m' + ': '))

                if opcion != 1 and opcion != 2:
                    raise ValueError
                break
            except:
                print(f"La opción no es válida. Intente nuevamente")

    if opcion == 1:
        opcion = "PUEDE CONTINUAR"
    else:
        opcion = "FIN DE JUEGO"

    return opcion
