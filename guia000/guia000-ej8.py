'''
8. En Años anteriores, se necesitaba una función en python que reciba un texto conteniendo bits (simbolos 1 y 0),
 y debia armar una lista conteniendo 8 bits por elementos (1 byte). Por ejemplo, si se incova la funcion con el
  siguiente texto como parámetro: "1001010101000101010101100101001010101010"
la funcion devuelve: ['10010101', '01000101', '01010110', '01010010', '10101010']

El programador de ese momento armó el siguiente código:
'''

#Definicion de las funciones
def validacion(texto):
    """
    Permite validar el texto binario
    :param texto: String de numeros binarios
    :return: Un bolleano con True or False
    """
    bandera = False
    for caracter in texto:
        if caracter != '0'  and caracter != '1':
            bandera = True
    if bandera == True:
        print("El texto ingresado no es binario")
    return bandera

def ej08a(texto):
    """Arma una lista de bytes acorde al texto recibido por parametro"""
    indice = 0
    resultado = []
    current_byte = ""

    for i in texto:
        current_byte += i  # se agrega el nuevo caracter al byte actual
        indice += 1  # se incrementa en uno el indice
        if indice % 8 == 0:
            # Comienza un nuevo byte
            resultado.append(current_byte)
            current_byte = ""
    return resultado

#Cuerpo del programa
texto = "111101010100010101010110010100101011101"


while validacion(texto) != False:             #Aqui valido el texto, y si no es valido solicito se ingrese uno válido
    texto = input('Ingrese un texto binario: ')

print(ej08a(texto))

