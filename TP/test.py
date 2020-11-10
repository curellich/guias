from blackjack import configuracion
from blackjack import interfaces
from blackjack import cartas
from blackjack import logica
import unittest


class Test_Suma_Cartas(unittest.TestCase):

    def test_suma_cartas(self):
        # Pruebo el comportamiento de las cartas de la corte
        jugador = {'cartas': [{'valor': 4, 'palo': "pica"}, {'valor': "K", 'palo': "diamante"}]}
        self.assertEqual((logica.suma_cartas(jugador)), 14)

        # Pruebo el comportamiento de los ases
        jugador = {'cartas': [{'valor': "A", 'palo': "pica"}, {'valor': "A", 'palo': "diamante"}]}
        self.assertEqual((logica.suma_cartas(jugador)), 12)

        # Pruebo el comportamiento de las cartas de la corte y los Ases
        jugador = {'cartas': [{'valor': "A", 'palo': "pica"}, {'valor': "K", 'palo': "diamante"},
                              {'valor': "J", 'palo': "diamante"}]}
        self.assertEqual((logica.suma_cartas(jugador)), 21)

        # Pruebo el comportamiento de las cartas de la corte y los Ases
        jugador = {'cartas': [{'valor': "K", 'palo': "pica"}, {'valor': "A", 'palo': "diamante"}]}  # (K + A) = 21
        self.assertEqual((logica.suma_cartas(jugador)), 21)


class Test_cpu_arriesgado(unittest.TestCase):

    def test_cpu_arriesgado(self):
        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 5, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'HUMANO', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 'A', 'palo': '♠'}, {'valor': 10, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 11
        # Cartas de Gonzalo suman 11 DEBERIA PEDIR CARTA
        # Cartas de Pepe suman 21

        nombre_jugador = "GONZALO"

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PEDIR CARTA")

        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 5, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 4, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'HUMANO', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♠'}, {'valor': 6, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 11
        # Cartas de Gonzalo suman 13 DEBERIA PEDIR CARTA
        # Cartas de Pepe suman 8

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PEDIR CARTA")

        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 5, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 4, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'HUMANO', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♠'}, {'valor': 6, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 11
        # Cartas de Gonzalo suman 13 -DEBERIA PEDIR CARTA
        # Cartas de Pepe suman 8

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PEDIR CARTA")

        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 5, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 9, 'palo': '♥'}, {'valor': 9, 'palo': '♠'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'HUMANO', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♠'}, {'valor': 6, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 11
        # Cartas de Gonzalo suman 18 -DEBERIA PEDIR CARTA
        # Cartas de Pepe suman 8

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PLANTARME")


class Test_cpu_prudente(unittest.TestCase):

    def test_cpu_prudente(self):
        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 5, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'HUMANO', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 'A', 'palo': '♠'}, {'valor': 10, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 11 --> DEBERIA PEDIR CARTA
        # Cartas de Gonzalo suman 11
        # Cartas de Pepe suman 21

        nombre_jugador = "JONATHAN"

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PEDIR CARTA")

        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 8, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 4, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'HUMANO', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♠'}, {'valor': 6, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 14 --> DEBERIA PEDIR CARTA
        # Cartas de Gonzalo suman 13
        # Cartas de Pepe suman 8

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PEDIR CARTA")

        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 5, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 4, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'HUMANO', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♠'}, {'valor': 6, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 11 -->DEBERIA PEDIR CARTA
        # Cartas de Gonzalo suman 13
        # Cartas de Pepe suman 8

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PEDIR CARTA")


class Test_cpu_inteligente(unittest.TestCase):

    def test_cpu_prudente(self):
        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 5, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'INTELIGENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 'A', 'palo': '♠'}, {'valor': 10, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 11
        # Cartas de Gonzalo suman 11
        # Cartas de Pepe suman 21 -->DEBERIA PLANTARSE

        nombre_jugador = "PEPE"

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PLANTARME")

        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 8, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 4, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'INTELIGENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 2, 'palo': '♠'}, {'valor': 6, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 14
        # Cartas de Gonzalo suman 13
        # Cartas de Pepe suman 8 -->DEBERIA PEDIR CARTA

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PEDIR CARTA")

        config_partida = [{'nombre': 'BANCA', 'cant_jugadores': 3, 'cant_barajas': 4, 'modo_juego': 'DIFICIL',
                           'juego_banca': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1000200.0,
                           'cartas': [{'valor': 10, 'palo': '♥'}]},
                          {'numero': 1, 'nombre': 'JONATHAN', 'cpu': 'PRUDENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 6, 'palo': '♣'}, {'valor': 5, 'palo': '♥'}]},
                          {'numero': 2, 'nombre': 'GONZALO', 'cpu': 'ARRIESGADO', 'estado': 'EN JUEGO', 'saldo': 400.0,
                           'posicion': None, 'cartas': [{'valor': 4, 'palo': '♥'}, {'valor': 9, 'palo': '♥'}]},
                          {'numero': 3, 'nombre': 'PEPE', 'cpu': 'INTELIGENTE', 'estado': 'EN JUEGO', 'saldo': 1200.0,
                           'posicion': None, 'cartas': [{'valor': 9, 'palo': '♠'}, {'valor': 9, 'palo': '♠'}]}]
        # Cartas de Jonathan suman 11
        # Cartas de Gonzalo suman 13
        # Cartas de Pepe suman 18 -->DEBERIA PLANTARSE

        self.assertEqual(logica.cpu_arriesgado(nombre_jugador, config_partida), "PLANTARME")


if __name__ == '__main__':
    unittest.main()
