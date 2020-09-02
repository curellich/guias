"""
3. Escribir una función que genere y retorne un diccionario ASCII. Para ello, las claves deben ser las letras a partir
 de la 'a' y el valor debe ser el número ASCII (a -> 97, b -> 98, ...).
Tips: se puede utilizar la función chr para convertir un número en su correspondiente letra o ord para la
situación inversa (conocer el valor ASCII de una letra). También recordar que se puede crear un diccionario vacío con
dict().
Resultado Esperado:
{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108,
 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120,
  'y': 121, 'z': 122}
"""


def generarDiccionarioAlfabetico():
    '''
    Funcion que genera un diccionario, teniendo como claves caracteres alfabeticos, y como valores, su valor correspondiente
    en ASCII
    :return: Devuelve un diccionario
    '''
    diccionario = {}
    for i in range(97, 122 + 1, 1):
        diccionario[chr(i)] = i
    return diccionario


diccionario = generarDiccionarioAlfabetico()

print(diccionario)
