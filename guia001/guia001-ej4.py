"""
4- Crear un programa que reciba del usuario la información de una fecha en formato dd/mm/aaaa y luego mostrar la
información desglosada.
Tip: analizar la función split aplicada a un string, donde se le especifica un separador.
Como resultado, se obtiene una lista (se puede verificar con type).
"""


def fechaALista(fecha):
    return fecha.split('/')


lista = fechaALista(input('Ingrese fecha con formato dd/mm/aaaa: '))
lista2 = ['dia', 'mes', 'anio']
for i in range(0, 2 + 1, 1):
    print(f'El {lista2[i]} ingresado es: {lista[i]}', )
