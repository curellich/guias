"""
9. Se necesita un programa que reciba por parámetro un texto, y que devuelva una tupla conteniendo en el primer lugar,
 la cantidad de letras (mayúsculas o minúsculas), en el segundo lugar la cantidad de dígitos numéricos y en el tercer
 lugar, otros símbolos.

Resultado Esperado (tupla): Por ejemplo, si se utiliza como parámetro el texto: "Esta es una mañana LLuviosa!!
25 días más serán así??" se debería obtener como resultado la tupla (38, 2, 13)
"""


# Definicion de las funciones
def cuentaCaracteres(texto):
    """
    Funcion que cuenta las letras, numeros y otrs simbolos de una cadena
    :param texto: Cadena de caracteres
    :return: Una tupla con (letras, numeros y otros simbolos
    """
    letras = 0
    numeros = 0
    otrosSimbolos = 0

    for caracter in texto:
        if caracter.isalpha() == True:
            letras += 1
        elif caracter.isdigit() == True:
            numeros += 1
        else:
            otrosSimbolos += 1
    return letras, numeros, otrosSimbolos


texto = "Esta es una mañana LLuviosa!! 25 días más serán así??"

print(cuentaCaracteres(texto))
