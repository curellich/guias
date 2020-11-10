from blackjack.constantes import CANT_MAX_JUGADORES, CANT_MAX_BARAJAS


# FRONTEND *
def validacion_cantidad_jugadores():
    """
    Funcion para validar el ingreso por teclado desde 1 hasta la constante CANT_MAX_JUGADORES
    :return: int con la opcion elegida
    """
    while True:
        try:
            cant_jugadores = int(input(
                'Ingrese la cantidad de jugadores ' + '\x1b[0;31;23m' + f'(1 - {CANT_MAX_JUGADORES})' + '\x1b[0m' + ':'))
            if cant_jugadores < 1 or cant_jugadores > CANT_MAX_JUGADORES:
                raise ValueError()
            break
        except ValueError:
            print(f"El numero de jugadores admitidos va \x1b[0;31;23m desde 1 hasta {CANT_MAX_JUGADORES}\x1b[0m")

    return cant_jugadores


# FRONTEND *
def validacion_canttidad_barajas():
    """
        Funcion para validar el ingreso por teclado desde 1 hasta la constante CANT_MAX_BARAJAS
        :return: int con la opcion elegida
        """
    while True:
        try:
            cant_barajas = int(input(
                'Ingrese la cantidad de barajas ' + '\x1b[0;31;23m' + f'(1 - {CANT_MAX_BARAJAS})' + '\x1b[0m' + ':'))
            if cant_barajas < 1 or cant_barajas > CANT_MAX_BARAJAS:
                raise ValueError()
            break
        except ValueError:
            print(f"El numero de barajas admitidas va \x1b[0;31;23m desde 1 hasta {CANT_MAX_BARAJAS} \x1b[0m")

    return cant_barajas


# FRONTEND *
def validacion_tipo_1_2():
    """
    Funcion para validar el ingreso por teclado para dos opciones 1 o 2
    :return: int la opcion elegida
    """
    while True:
        try:
            ingreso = int(input(
                'Ingrese la opcion ' + '\x1b[0;31;23m' + '(1-2)' + '\x1b[0m: '))
            if ingreso < 1 or ingreso > 2:
                raise ValueError()
            break
        except ValueError:
            print('El numero debe ser \x1b[0;31;23m "1" \x1b[0m o \x1b[0;31;23m "2" \x1b[0m')

    return ingreso


# FRONTEND *
def validacion_tipo_1_3():
    """
      Funcion para validar el ingreso por teclado para dos opciones 1,2 o 3
      :return: int la opcion elegida
      """
    while True:
        try:
            ingreso = int(input(
                "Ingrese el modo de juego de la banca: \x1b[0;31;23m 1- \x1b[0m Agresiva \x1b[0;31;23m 2- \x1b[0m "
                "Prudente \x1b[0;31;23m 3- \x1b[0m Inteligente: "))
            if ingreso < 1 or ingreso > 3:
                raise ValueError()
            break
        except ValueError:
            print("El numero admitido  \x1b[0;31;23m va desde 1 hasta 3 \x1b[0m ")

    return ingreso


# FRONTEND *
def validacion_tipo_1_4():
    """
          Funcion para validar el ingreso por teclado para dos opciones 1,2,3 o 4
          :return: int la opcion elegida
          """
    while True:
        try:
            ingreso = int(
                input(
                    'Ingrese el modo de juego: \x1b[0;31;23m 1- \x1b[0m CPU-Arriesgado, \x1b[0;31;23m 2- \x1b[0m CPU-Prudente, \x1b[0;31;23m 3- \x1b[0m Humano, \x1b[0;31;23m 4- \x1b[0m Inteligente: '))
            if ingreso < 1 or ingreso > 4:
                raise ValueError()
            break
        except ValueError:
            print('El numero admitito va \x1b[0;31;23m desde 1 hasta 4 \x1b[0m')

    return ingreso


# FRONTEND *
def validacion_tipo_1_contador(contador):
    """
    Funcion para validar el ingreso por teclado desde 1 hasta un limite puesto por contador
    :param contador: int con el valor limite
    :return: int con el valor ingresado por teclado
    """
    while True:
        try:
            opcion = int(input(f'Seleccione la partida a cargar:' '\x1b[0;31;23m' + f'(1-{contador}): ' + '\x1b[0m'))

            if opcion < 1 or opcion > contador:
                raise ValueError
            break
        except ValueError:
            print(f"La opción no es válida. Intente nuevamente")

    return opcion
