"""
2- Modificar la función anterior de forma tal que en vez de imprimir, genere y devuelva el string formateado.
Luego, al ser invocada, imprimir el resultado. (no debería sufrir ningún cambio visual).
"""

#Definiciones de funciones

def crear_mes(nombre, abreviatura, cantidadDeDias):
    return str(nombre),str(abreviatura), str(cantidadDeDias)

tupla= crear_mes('Enero', 'ENE', 31)

print(f'Se creo el mes {0}, que se abrevia {1} y contiene {2} días'.format(tupla[0],tupla[1],tupla[2]))

