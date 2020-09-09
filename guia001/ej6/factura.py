"""
La siguiente funcion ofrece al usuario la opcion de facturar productos creando una lista que despues utiliza la funcion
impresion_factura para mostrar los datos por pantalla
"""

from ej6.impresion_factura import imprimir_factura


# Este modulo de busqueda podria reemplazarse por el modulo buscar, pero no quiero que imprima el producto
def busqueda(catalogo, codigo):
    dicc = {}
    for producto in catalogo:
        if producto['codigo'] == codigo:  # Recorre de forma secuencial el catalogo y si encuentra el producto devuelve
            dicc = producto  # un diccionario
    if dicc != {}:
        return dicc
    else:  # Si el producto no existe, lo imprime y devuelve un false
        print("El producto no existe")
        print('-' * 80)
        return False


def facturar(catalogo):
    lista_productos = []  # En esta lista se van a guardar todos los PEDIDOS
    print('-' * 5 + 'FACTURACION' + '-' * 5)
    codigo = input('Ingrese codigo de producto o "F" Para imprimir la factura: ')


    while codigo != 'f' and codigo != 'F' and codigo != '':
        producto = busqueda(catalogo, (int(codigo)))  # Utiliza la funcion buscar, si devolvio un diccionario es porque

        if isinstance(producto, dict) == True:  # el producto fue encontrado. Y lo agrega a la lista
            # Aqui valido el ingreso como un valor entero
            while True:
                try:
                    producto['cantidad'] = int(
                        input('Ingrese la cantidad deseada: '))  # Agrego la cantidad al diccionario
                    break
                except ValueError:
                    print('La cantidad ingresada no es un NUMERO')

            lista_productos.append(producto)

        codigo = input('Ingrese codigo de producto o "F" para imprimir la factura: ')

    imprimir_factura(lista_productos)  # Aqui imprimo la factura y finaliza la funcion
