from blackjack import configuracion
from blackjack import interfaces
from blackjack import cartas
from blackjack import logica

# Cartel de bienvenida
interfaces.cartel_bienvenida()

# El jugador decide si cargar partida o realizar un juego nuevo
desicion = interfaces.menu_inicial()

# Lista de perdedores para almacenar los jugadores que se quedan sin saldo
lista_perdedores = []

# Lista de ganadores para almacenar los jugadores que superan el saldo maximo
lista_ganadores = []

# Bandera para controlar cuando termina el juego
control = ""

# Si la opcion fue configurar el juego nuevo...
if desicion == "Juego Nuevo":
    # Se muestra por pantalla el cartel de configuracion del juego
    interfaces.cartel_configuracion_juego()

    # Se crea la lista de configuracion del juego sobre la que trabaja el programa
    config_partida = configuracion.config_partida_inicial(configuracion.config_juego())

    # Se crea el archivo y se guarda el nombre del archivo en el fichero partidas.txt
    nombre_archivo = configuracion.crear_archivo_partida(config_partida)
    configuracion.guardar_nombre_en_archivo(nombre_archivo)

    # Se prepara el/los masos para jugar
    maso_de_juego = cartas.maso_de_juego(config_partida)

    # Se reparte las cartas a los jugadores y a la banca
    cartas.barajar(config_partida, maso_de_juego)
    cartas.carta_escondida_banca(config_partida)

    # Se muestran las cartas de la mesa
    interfaces.cartel_cartas_en_la_mesa()
    interfaces.mostrar_cartas_mesa(config_partida)

    # Si la opcion fue cargar patida...
else:
    # Se carga una partida guardada
    nombre_archivo = interfaces.menu_cargar_partida()
    config_partida = configuracion.cargar_partida_de_archivo(nombre_archivo)

    # Se filtra los jugadores que no tienen saldo para jugar
    lista_perdedores = logica.eliminacion_perdedores(config_partida)

    # Se filtra los jugadores que superen el saldo maximo de juego (ganadores )
    lista_ganadores = logica.eliminacion_ganadores(config_partida)

    # Si existen ganadores por haber superado el saldo maximo o todos son perdedores por quedarse sin saldo
    # Se muestra la tabla y se finaliza el juego
    if len(lista_ganadores) != 0 or len(config_partida) == 1:
        interfaces.mostrar_tabla(config_partida, lista_perdedores, lista_ganadores)
        print("\x1b[0;37;31m Esta partida está FINALIZADA \x1b[0m")
        exit()

    # Se muestra la tabla
    interfaces.mostrar_tabla(config_partida, lista_perdedores, lista_ganadores)

    # Se prepara el/los masos para jugar
    maso_de_juego = cartas.maso_de_juego(config_partida)

    # Se borran las cartas que tengan todos los jugadores
    configuracion.limpiar_cartas(config_partida)

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
                interfaces.mostrar_jugada(jugadores['nombre'], config_partida, maso_de_juego)
                logica.pause()
                print("-" * 50 + "\n")
            else:
                interfaces.mostrar_jugada(jugadores['nombre'], config_partida, maso_de_juego)
                logica.pause()
                print("-" * 50 + "\n")

    # Juega la BANCA
    interfaces.mostrar_jugada("BANCA", config_partida, maso_de_juego)
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

    # Se filtra los jugadores que superen el saldo maximo de juego (ganadores )
    lista_ganadores = logica.eliminacion_ganadores(config_partida)

    # Se borran (retiran) las cartas que tengan todos los jugadores
    configuracion.limpiar_cartas(config_partida)

    # Sobreescribo partida en el archivo.
    configuracion.sobreescribir_archivo_partida(nombre_archivo, config_partida, lista_perdedores, lista_ganadores)

    # Muestro tabla de  saldos y estados
    interfaces.mostrar_tabla(config_partida, lista_perdedores, lista_ganadores)

    # Analizo que que no se cumplan las condiciones 1) y 2) para  poder continuar el juego
    control = logica.analisis_continuidad_juego(config_partida, lista_ganadores)

    # Si hay algun ganador/es del juego se muestra por pantalla
    if control == "FIN DE JUEGO":
        interfaces.mostrar_ganador_juego(config_partida)

    # Si estan las condiciones para continuar es decir que no estemos en el caso 1) o caso 2),

    if control != "FIN DE JUEGO":
        # Le pregunto al usuario si desea continuar o salir del juego
        control = interfaces.cierre_juego(config_partida, lista_ganadores)

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
