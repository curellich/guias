"""
Con esta funcion busco un producto dentro del catalogo productos.py, e imprimo por pantalla la informacion del producto.
"""


def buscar(catalogo, numero):
    dicc = {}
    for producto in catalogo:
        if producto['codigo'] == numero:
            dicc = producto
    if dicc != {}:
        print('-' * 80)
        print('El producto buscado es el siguiente:')
        print(dicc)
        print('-' * 80)
        return True
    else:
        print("El producto no existe")
        print('-' * 80)
        return False
