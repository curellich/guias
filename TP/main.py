from blackjack import configuracion
from blackjack import interfaces
from blackjack import cartas
from blackjack import logica

# Cartel de bienvenida
interfaces.cartel_bienvenida()

# El jugador decide si cargar partida o realizar un juego nuevo
desicion = interfaces.menu_inicial()

# Se carga la partida o se configura el juego nuevo
if desicion == "Juego Nuevo":
    # Se crea la lista de configuracion del juego sobre la que trabaja el programa
    config_partida = configuracion.config_partida_inicial(configuracion.config_juego())

    # Se crea el archivo y se guarda el nombre del archivo en el fichero partidas.txt
    configuracion.guardar_nombre_en_archivo(configuracion.crear_archivo_partida(config_partida))

    # Se prepara el/los masos para jugar
    maso_de_juego = cartas.maso_de_juego(config_partida)

    # Se reparte las cartas a los jugadores y se quita una carta a la banca
    cartas.barajar(config_partida,maso_de_juego)
    cartas.carta_escondida_banca(config_partida)

    #Se muestran las cartas de la mesa
    interfaces.cartel_cartas_en_la_mesa()
    interfaces.mostrar_cartas_mesa(config_partida)
else:
    # Se carga una partida guardada
    nombre_archivo = interfaces.menu_cargar_partida()
    config_partida = configuracion.cargar_partida_de_archivo(nombre_archivo)

    # Se prepara el/los masos para jugar
    maso_de_juego = cartas.maso_de_juego(config_partida)

    #Se borran las cartas que tengan todos los jugadores
    configuracion.limpiar_cartas(config_partida)

    # Se reparte las cartas a los jugadores y se quita una carta a la banca
    cartas.barajar(config_partida,maso_de_juego)
    cartas.carta_escondida_banca(config_partida)

    # Se muestran las cartas de la mesa
    interfaces.cartel_cartas_en_la_mesa()
    interfaces.mostrar_cartas_mesa(config_partida)

