"""
6- Un supermercado requiere un sistema de facturación que pueda calcular los totales de las facturas que realizan
   las cajas registradoras. Cada caja ingresa el código del producto (numérico) y tiene una base de productos,
   ya codificada en la lista contenida del archivo productos.py
   Se pide realizar los siguientes requerimientos solicitados por el cliente:

a. Presentar un menú permitiendo al usuario elegir una de las siguientes opciones:
    1) Buscar producto
    2) Ingresar nueva factura
    3) Ingresar nuevo producto al catalogo
    3) Salir

b. Realizarf unción llamada buscar en el modulo productos.py de forma tal de recibir por parámetro un código numérico de
   producto y retornar el mismo, utilizando la lista de diccionarios implementada.

c. Juntar los dos puntos anteriores en el programa, de forma tal de implementar correctamente la opción 1,
   que permita al usuario buscar un producto y mostrar la información de este (se permite hacer print, pero
   puede también formatearse mediante format).

d. Continuar implementando la opción 2, la cual debe solicitar al usuario cada código de producto. Si el producto
   se encuentra en la lista, preguntar la cantidad. Si no se encuentra en el catalogo, informarlo por pantalla para
   volver a reingresar otro código de producto. Si ingresa ‘F’ se considera que finaliza la factura. Al finalizar,
   mostrar la factura, producto por producto, con la cantidad y el total de la factura.

   Tips: Repasar el tipo de datos lista (mediante la creación con list() o con []). Cada factura debe ser una
   lista nueva. Y mediante las operaciones de agregado (append) ir completándola.
e. Con la opción de agregar nuevo producto al catalogo,debe solicitarle los datos de descripción, y precio unitario con dos
   decimales. Luego agregarla al catalogo. Se aprecia si para este se crea una nueva función agregar en el modulo
   de productos.

   Utilizar módulos permitiendo la reutilización del código y no debe encontrarse toda la lógica en un solo archivo.
   Tips: Se agrega a continuación un ejemplo de obtención del catalogo dentro del modulo productos y su utilización,
   imprimiendo toda la información del mismo y utilizando la función format para incluir cada campo de los productos
"""


from ejercicio006.ej6 import buscar
from ejercicio006.ej6.productos import catalogo
from ejercicio006.ej6 import listar_productos

from ejercicio006.ej6 import menu

#Programa principal
opcion =''
while opcion != '5':
    opcion = str(menu())
    if opcion == '1':
        buscar(catalogo, int(input('Ingrese el numero del producto: ')))
    elif opcion == '2':
        listar_productos(catalogo)









