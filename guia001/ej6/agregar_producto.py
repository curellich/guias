"""
La siguiente funcion permite agregar productos al catalo de productos que esta en el modulo productos.py
"""

def agregar_producto(catalogo):
    print('-'*5+'AGREGANDO PRODUCTOS'+'-'*5+'\n')
    continuar = input('Presione cualquier letra para continua o "F" para salir')

    while continuar != 'F' and continuar != 'f':
        producto ={}
        # Aqui se valida el ingreso del nuevo producto
        while True:
            try:
                codigo = int(input('Ingrese el codigo del nuevo producto: '))
                break
            except ValueError:
                print('La cantidad ingresada no es un NUMERO')
        producto['codigo']= codigo
        desc= input('Ingrese la descripcion del producto')
        producto['desc'] = desc.title()
        while True:
            try:
                precio = float(input('Ingrese el precio del nuevo producto: '))
                break
            except ValueError:
                print('La cantidad ingresada no es un valida')
        producto['precio']= round(precio,2)
        catalogo.append(producto)
        print("!!!PRODUCTO AGREGARO¡¡¡")
        continuar = input('Presione cualquier letra para continua o "F" para salir')

