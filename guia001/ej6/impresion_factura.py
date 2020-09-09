"""
En esta funcion se recibe una lista de diccionarios, e imprime la cantidad, productos, precio, subtotal y por ultimo
el total facturado
"""


def imprimir_factura(lista_productos):
    total = 0
    print('-' * 80)
    print('-' * 3 + ' FACTURA DEL PEDIDO REALIZADO' + '-' * 3 + '\n')
    print('CANTIDAD      DESCRIPCION             PRECIO         SUBTOTAL')

    for i in lista_productos:  # Recorro toda la lista, y en cada diccionario ingreso por la key
        print(i.get('cantidad'), end='\t\t\t')
        print(i.get('desc'), end='\t\t')
        print(i.get('precio'), end='\t\t')
        subtotal = int(i.get('cantidad')) * (i.get('precio'))
        total = total + subtotal  # Acumulo el total el lo imprimo al final
        print(subtotal)
    print('-' * 25 + f'El total facturado------>{float(total):.2f}')
    print(input('Presione ENTER para continuar:'))
