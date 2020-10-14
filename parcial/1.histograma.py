from mis_funciones import mis_funciones

nombre_archivo = "./mis_funciones/texto.txt"

# Manejo de exepcion: FileNotFoundError
try:
    with open(nombre_archivo) as f:
        texto = open(nombre_archivo, "rt")
except FileNotFoundError:
    print(f"El nombre del archivo {nombre_archivo} no existe ")
else:
    # creo la lista de palabras desde el texto
    lista_de_palabras = mis_funciones.listar_palabras(texto)

    # sanitizo la lista de palabras
    lista_de_palabras = mis_funciones.case_insensitive(lista_de_palabras)

    # creo un coleccion "conjuntos" para elimirar los elementos repetidos de las listas
    palabras = set(lista_de_palabras)

    # creo una lista de palabras ordenadas no repetidas
    palabras_ordenadas = mis_funciones.ordenar_lista(list(palabras))

    # Busco las veces que aparece cada palabra y las muestro por panatalla de forma ordenada
    for palabra in palabras_ordenadas:
        print("{}: {}".format(palabra, lista_de_palabras.count(palabra)))
