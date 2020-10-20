from blackjack import configuracion
from blackjack import interfaces
from blackjack import cartas
from blackjack import logica

# Cartel de bienvenida
interfaces.cartel_bienvenida()

# El jugador decide si cargar partida o realizar un juego nuevo
desicion = interfaces.menu_inicial()

# Variable para controlar cuando termina el juego
control = ""

# Se carga la partida o se configura el juego nuevo
if desicion == "Juego Nuevo":
    # Se muestra por pantalla el cartel de configuracion del juego
    interfaces.cartel_configuracion_juego()

    # Se crea la lista de configuracion del juego sobre la que trabaja el programa
    config_partida = configuracion.config_partida_inicial(configuracion.config_juego())

    # Se crea la lista de perdedores para almacenar los que se quedan sin saldo
    lista_perdedores = []

    # Se crea el archivo y se guarda el nombre del archivo en el fichero partidas.txt
    nombre_archivo = configuracion.crear_archivo_partida(config_partida)
    configuracion.guardar_nombre_en_archivo(nombre_archivo)

    # Se prepara el/los masos para jugar
    maso_de_juego = cartas.maso_de_juego(config_partida)

    # Se reparte las cartas a los jugadores y se quita una carta a la banca
    cartas.barajar(config_partida, maso_de_juego)
    cartas.carta_escondida_banca(config_partida)

    # Se muestran las cartas de la mesa
    interfaces.cartel_cartas_en_la_mesa()
    interfaces.mostrar_cartas_mesa(config_partida)
else:
    # Se carga una partida guardada
    nombre_archivo = interfaces.menu_cargar_partida()
    config_partida = configuracion.cargar_partida_de_archivo(nombre_archivo)

    # Se filtra los jugadores que no tienen saldo para jugar
    lista_perdedores = logica.eliminacion_perdedores(config_partida)

    # Se prepara el/los masos para jugar
    maso_de_juego = cartas.maso_de_juego(config_partida)

    # Se borran las cartas que tengan todos los jugadores
    configuracion.limpiar_cartas(config_partida)

    # Se muestra la tabla
    interfaces.mostrar_tabla(config_partida, lista_perdedores)

    # Se reparte las cartas a los jugadores y se quita una carta a la banca
    cartas.barajar(config_partida, maso_de_juego)
    cartas.carta_escondida_banca(config_partida)

    # Se muestran las cartas de la mesa
    interfaces.cartel_cartas_en_la_mesa()
    interfaces.mostrar_cartas_mesa(config_partida)

# Hasta aca ya tengo lo que necesito para INICIAR las partidas de HUMANO o CPU
# La lista con la configuracion de la partida (JUGADORES, SALDO, ESTADOS Y CARTAS EN LA MESA)
# El MASO de juego a esta altura tiene las cantidad de barajas configuradas MENOS las cartas repartidas a los jugadores

# El ciclo de juego se va a desarrollar mientras:
#  1) NO HAYA UN GANADOR (que supere el monto maximo establecido en las CONSTANTES)
#  2) Exista un jugador con su estado EN JUEGO (es decir que por lo menos haya un jugador con saldo contra la banca)
#  3) El usuario no quiera interrumpir antes el juego.

while control != "FIN DE JUEGO":
    # Juegan todos los jugadores menos la BANCA
    for jugadores in config_partida:
        if jugadores['nombre'] != "BANCA":
            if jugadores['cpu'] == "HUMANO":
                interfaces.jugada_humano(jugadores['nombre'], config_partida, maso_de_juego)
                logica.pause()
                print("-" * 50 + "\n")
            else:
                interfaces.mostrar_jugada_cpu(jugadores['nombre'], config_partida, maso_de_juego)
                logica.pause()
                print("-" * 50 + "\n")

    # Juega la BANCA
    interfaces.mostrar_jugada_banca("BANCA", config_partida, maso_de_juego)
    logica.pause()

    # Analizo las cartas que salieron en la mesa y acutalizo los estados a GANA o PIERDE
    logica.actualizacion_estados(config_partida)

    # Muestro el/los ganador/es de la ronda
    interfaces.mostrar_ganadores_ronda(config_partida)

    # Actualizo los saldos para ganadores y perdedores
    logica.actualizacion_saldos(config_partida)

    # Analizo continuidad de los jugadores en base a su saldo disponible
    for jugadores in config_partida:
        logica.analisis_continuidad_jugador(jugadores)

    # Elimino los jugadores que no pueden continuar jugando por falta de saldo
    lista_perdedores.extend(logica.eliminacion_perdedores(config_partida))

    # Se borran (retiran) las cartas que tengan todos los jugadores
    configuracion.limpiar_cartas(config_partida)

    # Sobreescribo partida en el archivo.
    configuracion.sobreescribir_archivo_partida(nombre_archivo, config_partida)

    # Muestro tabla de  saldos y estados
    interfaces.mostrar_tabla(config_partida, lista_perdedores)

    # Si estan las condiciones para continuar es decir que no estemos en el caso 1) o caso 2),
    # le pregunto al usuario si desea continuar o salir del juego
    control = logica.analisis_continuidad_juego(config_partida)
    if control != "FIN DE JUEGO":
        control = interfaces.cierre_juego(config_partida)
        if control != "FIN DE JUEGO":
            # si el juego continua....
            # Se prepara el/los masos para jugar
            maso_de_juego = cartas.maso_de_juego(config_partida)

            # Se reparte las cartas a los jugadores y se quita una carta a la banca
            cartas.barajar(config_partida, maso_de_juego)
            cartas.carta_escondida_banca(config_partida)

            # Se muestran las cartas de la mesa
            interfaces.cartel_cartas_en_la_mesa()
            interfaces.mostrar_cartas_mesa(config_partida)

            # reinicia la ronda
