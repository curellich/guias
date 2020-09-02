'''
6. Se necesita un programa que reciba por línea de comando una serie de palabras, hasta que reciba la palabra "exit".
Una vez recibida dicha instrucción, debe mostrar por salida standard las mismas palabras ingresadas, almacenadas en
una lista, pero ordenadas alfabéticamente y cada una debe estar capitalizada.
Resultado Esperado: El programa le solicita al usuario que ingrese y este escribe:
Ingrese palabra: hola
Ingrese palabra: QUE
Ingrese palabra: tal
Ingrese palabra: como
Ingrese palabra: estas
Ingrese palabra: exit
Se espera recibir el siguiente resultado: ['Como', 'Estas', 'Hola', 'Que', 'Tal']
'''

lista = []
texto = 'NULL'
while texto != 'Exit':
    texto = input('Ingrese palabra: ').capitalize()
    lista.append(texto)

print(sorted(lista))
