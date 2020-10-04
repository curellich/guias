def crear_baraja(archivo):
    """
    La funcion crea la baraja, dependiendo de la cantidad configurada
    :param archivo: str con el nombre del archivo de la partida
    :return: list con las cartas
    """
    baraja_tipo = []
    carta = {'valor': None, 'palo': None}
    palos = ["P", "D", "T", "C"]
    valores = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    for i in valores:
        for j in palos:
            carta['valor'] = i
            carta['palo'] = j
            baraja_tipo.append(carta)

    return baraja_tipo



nueva_baraja = crear_baraja("jona")
print(nueva_baraja[0].get('palo'))
