'''
2. Escribir la función factorial, que reciba como parámetro el numero inicial y compute su resultado.
a. Ejemplo factorial(8) = 8*7*6*5*4*3*2*1 = 40320. Recuerde que factorial de 0 por definición es 1.
b. Hacer la implementación inversa (si lo hizo recursivo, hacerlo iterativo o viceversa)
'''


def factorial(numero):
    '''
    La funcion devuelve el factorial de un numero
    :param numero:Valor entero a calcular el factorial
    :return:Devuelve el factorial del numero (entero)
    '''
    if numero == 0 or numero == 1:
        resultado = 1
    elif numero > 1:
        resultado = numero
        while numero != 1:
            resultado = resultado * (numero - 1)
            numero -= 1
    return resultado


def factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        resultado = 1
    elif numero > 1:
        resultado = numero * factorial(numero - 1)
    return resultado


cadena = " El factorial del numero {0} es: {1}, y calculado con recursividad es {2}"
print(cadena.format(8, factorial(8), factorial_recursivo(8)))
