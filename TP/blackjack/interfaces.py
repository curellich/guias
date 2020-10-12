from blackjack.cartas import sacar_carta
from blackjack.logica import suma_cartas
from blackjack.logica import cpu_arriesgado
from blackjack.logica import cpu_prudente
from blackjack.logica import cpu_inteligente
from blackjack.cartas import formato_carta
from blackjack.logica import analisis_continuidad_juego
from blackjack.configuracion import comprobacion_fichero


# BACKEND *
def cartel_bienvenida():
    """
    Funcion que imprime el encabezado del juego
    :return:
    """
    print("""    +++++++++++++++++++++++++++++++++++++++++++++
        +                                           +
        +         BIENBENIVO AL BLACKJACK           +
        +                                           +
        +++++++++++++++++++++++++++++++++++++++++++++""")
    return None


# BACKEND *
def cartel_configuracion_juego():
    """
    Funcion que imprime el encabezado del juego
    :return:
    """
    print("""    +++++++++++++++++++++++++++++++++++++++++++++
        +         Configuración del Juego           +
        +++++++++++++++++++++++++++++++++++++++++++++""")
    return None


# BACKEND *
def cartel_cartas_en_la_mesa():
    """
    Funcion que imprime el encabezado del juego
    :return:
    """
    print("""    +++++++++++++++++++++++++++++++++++++++++++++
        +         Cartas en  el mesa           +
        +++++++++++++++++++++++++++++++++++++++++++++""")
    return None


# FRONTEND *
def menu_inicial():
    """
    Funcion que muestra un menu y permite decidir si se inicia un juego nuevo o se carga una partida
    :return: int con la opcion seleccionada
    """
    indicador = comprobacion_fichero()

    if indicador == "VACIO":
        # no existen partidas grabadas
        print("No existen partidas anteriores!!! \n")
        resultado = "Juego Nuevo"
    else:
        # si existe partidas grabadas
        print("Seleccione la opcion deseada: ")
        print("""
                1- Cargar Partida
                2- Juego Nuevo
                """)

        while True:
            try:
                opcion = int(input('Opción (1-2): '))

                if opcion != 1 and opcion != 2:
                    raise ValueError
                break
            except:
                print(f"La opción no es válida. Intente nuevamente")

        if opcion == 1:
            resultado = "Cargar Partida"
        else:
            resultado = "Juego Nuevo"

    return resultado


# FRONTEND

def menu_cargar_partida():
    """
    Funcion que pide el nombre del archivo para vargar la partida
    :return: str con el nombre del archivo
    """
    fichero = open("./blackjack/partidas.txt", "r")
    lista = fichero.readlines()
    fichero.close()

    print("Las partidas guardadas son:")
    contador = 0
    for partida in lista:
        print(f"{contador + 1}", partida)
        contador = contador + 1
    print("\n")
    while True:
        try:
            opcion = int(input(f"Seleccione la partida a cargar: (1-{contador}): "))

            if opcion < 1 or opcion > contador:
                raise ValueError
            break
        except:
            print(f"La opción no es válida. Intente nuevamente")
    nombre_fichero = str(lista[opcion - 1]).rstrip()
    return nombre_fichero


# FRONTEND *
def menu_jugador_humano(config_partida):
    """
    Funcion que muestra el menu de juego al jugador.
    :return: Opcion
    """
    print("""
    1- Pedir carta
    2- Plantarme 
    """)

    while True:
        try:
            opcion = int(input('Opción (1-2): '))

            if opcion != 1 and opcion != 2:
                raise ValueError
            break
        except:
            print(f"La opción no es válida. Intente nuevamente")

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
    Funcion que imprime por pantalla las cartas de un jugador, ya sea humano o maquina
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
    Funcion que desarrolla la jugada de un jugador humano, las cartas recibidas se agregan a la config_juego
    :param nombre_jugador: str con el nombre del jugador
    :param config_partida: list con la configuracion del juego
    :param maso: list con las cartas que se estan jugando
    :return:
    """
    jugador = {}
    for jugadores in config_partida:
        if nombre_jugador == jugadores['nombre']:
            jugador = jugadores

    print(f"Turno : {nombre_jugador}", end=' --> Cartas: ')
    # muestro las cartas del jugador
    mostrar_cartas_jugada(nombre_jugador, config_partida)
    # muestro las opciones de juego
    opcion = str(menu_jugador_humano(config_partida))  # se muestran las opciones juagar o plantarse

    # si pidió cartas
    if opcion == "PEDIR CARTA":
        carta_nueva = sacar_carta(maso)
        jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
        print("Cartas: ", end='')
        mostrar_cartas_jugada(nombre_jugador, config_partida)

    while opcion != "PLANTARME" and suma_cartas(jugador) < 21:  #
        opcion = menu_jugador_humano(config_partida)
        if opcion == "PLANTARME":
            print("\n")
            break
        carta = sacar_carta(maso)
        jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
        print("Cartas: ", end='')
        mostrar_cartas_jugada(nombre_jugador, config_partida)

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
    jugador = {}
    for jugadores in config_partida:
        if nombre_jugador == jugadores['nombre']:
            jugador = jugadores

    print(f"Turno : {nombre_jugador} ({jugador['cpu']})", end=' --> Cartas: ')
    # muestro las cartas del jugador
    mostrar_cartas_jugada(nombre_jugador, config_partida)

    # DESARROLLO DEL JUEGO PARA EL CPU ARRIESGADO
    if jugador['cpu'] == 'ARRIESGADO':
        opcion = cpu_arriesgado(jugador['nombre'], config_partida)
        print(f"\nCPU decide--> {opcion}")

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_arriesgado(jugador['nombre'], config_partida)
                print(f"\nCPU decide--> {opcion}")
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)

    # DESARROLLO DEL JUEGO PARA CPU PRUDENTE
    elif jugador['cpu'] == 'PRUDENTE':
        opcion = cpu_prudente(jugador['nombre'], config_partida)
        print(f"\nCPU decide--> {opcion}")

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_prudente(jugador['nombre'], config_partida)
                print(f"\nCPU decide--> {opcion}")
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)

    # DESARROLLO DEL JUEGO PARA CPU INTELIGENTE
    elif jugador['cpu'] == 'INTELIGENTE':
        opcion = cpu_inteligente(jugador['nombre'], config_partida)
        print(f"\nCPU decide--> {opcion}")

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_inteligente(jugador['nombre'], config_partida)
                print(f"\nCPU decide--> {opcion}")
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)

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

    print(f"Turno : {nombre_jugador} ({jugador['juego_banca']})", end=' --> Cartas: ')
    # muestro las cartas del jugador
    mostrar_cartas_jugada(nombre_jugador, config_partida)

    # DESARROLLO DEL JUEGO PARA EL BANCA ARRIESGADO
    if jugador['juego_banca'] == 'ARRIESGADO':
        opcion = cpu_arriesgado(jugador['nombre'], config_partida)
        print(f"\nBANCA decide--> {opcion}")

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_arriesgado(jugador['nombre'], config_partida)
                print(f"\nBANCA decide--> {opcion}")
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)

    # DESARROLLO DEL JUEGO PARA BANCA PRUDENTE
    elif jugador['juego_banca'] == 'PRUDENTE':
        opcion = cpu_prudente(jugador['nombre'], config_partida)
        print(f"\nBANCA decide--> {opcion}")

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_prudente(jugador['nombre'], config_partida)
                print(f"\nBANCA decide--> {opcion}")
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)

    # DESARROLLO DEL JUEGO PARA BANCA INTELIGENTE
    elif jugador['juego_banca'] == 'INTELIGENTE':
        opcion = cpu_inteligente(jugador['nombre'], config_partida)
        print(f"\nBANCA decide--> {opcion}")

        # si pidió cartas
        if opcion == "PEDIR CARTA":
            carta_nueva = sacar_carta(maso)
            jugador['cartas'].append(carta_nueva)  # agrega la carta a sus cartas de la configuracion del juego
            print("Cartas: ", end='')
            mostrar_cartas_jugada(nombre_jugador, config_partida)

            while opcion != "PLANTARME" and suma_cartas(jugador) < 21:
                opcion = cpu_inteligente(jugador['nombre'], config_partida)
                print(f"\nBANCA decide--> {opcion}")
                if opcion == "PLANTARME":
                    print("\n")
                    break
                carta = sacar_carta(maso)
                jugador['cartas'].append(carta)  # agrega la carta a sus cartas de la configuracion del juego
                print("Cartas: ", end='')
                mostrar_cartas_jugada(nombre_jugador, config_partida)

    return


# FRONTEND *
def mostrar_ganadores_ronda(config_partida):
    """
    Funcion que imprime por pantalla el/los jugadores ganadores que reciben premio
    :param config_partida: list con la configuracion del juego
    :return: None
    """

    for jugadores in config_partida:
        if jugadores['estado'] == "GANA":
            print(f"{jugadores['nombre']} GANA!!!")


# FRONTEND *
def mostrar_tabla(config_partida, lista_perdedores):
    """
    Funcion que muestra jugadores, saldos y estados. Ordenados por saldo
    :param config_partida: list con la config_partida
    :return:
    """
    cabecera = ('JUGADOR', 'SALDO', 'ESTADO')

    # imprimo la cabecera de la tabla
    print(f'|{"-" * 18:^20} |', f'{"-" * 18:^20} |', f'{"-" * 18:^20} |')
    print(f'|{cabecera[0]:^20} |', f'{cabecera[1]:^20} |', f'{cabecera[2]:^20} |')
    print(f'|{"-" * 18:^20} |', f'{"-" * 18:^20} |', f'{"-" * 18:^20} |')

    # imprimo los datos de cada jugador en juego
    for jugadores in config_partida:
        if jugadores['nombre'] == "BANCA":
            continue
        else:
            print(f"|{jugadores['nombre']:^20} |", f"{jugadores['saldo']:^20} |", f"{jugadores['estado']:^20} |")

    if len(lista_perdedores) != 0:
        print(f'|{"-" * 18:^20} |', f'{"-" * 18:^20} |', f'{"-" * 18:^20} |')
        for perdedores in lista_perdedores:
            print(f"|{perdedores['nombre']:^20} |", f"{perdedores['saldo']:^20} |", f"{perdedores['estado']:^20} |")
    print(f'|{"-" * 18:^20} |', f'{"-" * 18:^20} |', f'{"-" * 18:^20} |')

    return None


# FRONTEND
def cierre_juego(config_partida, lista_perdedores):
    """
    Funcion  mostrar por pantalla los resultados de la ronda o final del juego. El usuario decide continuar o no.
    :return: "FINALIZAR" o "CONTINUAR"
    """
    mostrar_tabla(config_partida, lista_perdedores)

    if analisis_continuidad_juego(config_partida) == "PUEDE CONTINUAR":
        print("-" * 3, "Presione 1 para continuar o 2 para finalizar el juego", "-" * 3)

        while True:
            try:
                opcion = int(input('Opción (1-2): '))

                if opcion != 1 and opcion != 2:
                    raise ValueError
                break
            except:
                print(f"La opción no es válida. Intente nuevamente")

    return opcion
