"""
El siguiente programa funciona como menu cumpliendo los siguientes requerimientos
6- Un supermercado requiere un sistema de facturación que pueda calcular los totales de las facturas que realizan
   las cajas registradoras. Cada caja ingresa el código del producto (numérico) y tiene una base de productos,
   ya codificada en la lista contenida del archivo productos.py
   Se pide realizar los siguientes requerimientos solicitados por el cliente:

a. Presentar un menú permitiendo al usuario elegir una de las siguientes opciones:
    1) Buscar producto
    2) Ingresar nueva factura
    3) Ingresar nuevo producto al catalogo
    3) Salir
"""
def menu():
    opcion = ''
    while not (opcion >= '1' and opcion <= '5'):
        print("""
        ------MENU PRINCIPAL-------
        Caja de Supermercado
        1) Buscar producto
        2) Mostrar lista de productos
        3) Ingresar nueva factura
        4) Ingresar nuevo producto 
        5) Salir
        """)
        opcion = (input('Por favor, seleccione una opción: '))
        if not (opcion >= '1' and opcion <= '5'):
            print('!!!La opción ingresada no es valida¡¡¡')
            opcion = (input('Por favor, seleccione una opción: '))
            print('-' * 80)
    return opcion



