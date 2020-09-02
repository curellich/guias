"""
Con esta funcion busco un producto dentro del catalogo productos.py, e imprimo por pantalla la informacion del producto.
"""

def buscar (catalogo,numero):
    dicc={}
    for producto in catalogo:
        if producto['codigo'] == numero:
            dicc=producto

    if dicc != {}:
        print('-'*50)
        print('El producto buscado es el siguiente:')
        print(dicc)
        print('-' * 50)
    else:
        print("El producto no existe")
        print('-' * 50 )

