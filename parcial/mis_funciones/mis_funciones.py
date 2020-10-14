from math import ceil


# BACKEND
def listar_palabras(texto):
    """
    Funcion que crea una lista de palabras a partir de un string, las separa por espacios en blanco
    :param texto: str con el texto
    :return: list con la lista de palabras separadas por espacioes en blanco
    """
    lista = []
    for renglon in texto:
        lista.extend(renglon.split())  # separo las palabras que se encuentran en cada renglon
    return lista


# BACKEND
def case_insensitive(lista_de_palabras):
    """
    Funcion que convierte a minusculas todas las palabras de la lista y elimina "." despues de la palabra.
    :param lista_de_palabras: list palabras
    :return: list sanitizada
    """
    lista_en_minuscula = []
    for palabra in lista_de_palabras:
        palabra = palabra.lower()
        lista_en_minuscula.append(palabra.replace(".", ""))
    return lista_en_minuscula


# BACKEND
def ordenar_lista(lista):
    """
    Funcion que retorna la lista ordenada
    :param lista: list desordenda
    :return: list ordenada
    """
    lista.sort()
    return lista


# BACKEND
def validar_contrasenia(contrasenia):
    """
    Funcion que analiza que la contraseña reuna las condiciones solicitadas
    :param contrasenia: str contrasenia
    :return: True si es valida o False si no es valida
    """
    cont_caracteres = 0
    cont_minusculas = 0
    cont_mayuscualas = 0
    cont_numeros = 0
    cont_simbolos = 0

    # acumulo  en los contadores correspondientes el caracter
    for i in contrasenia:
        cont_caracteres = cont_caracteres + 1
        if i.islower():
            cont_minusculas = cont_minusculas + 1
        elif i.isupper():
            cont_mayuscualas = cont_mayuscualas + 1
        elif i.isdigit():
            cont_numeros = cont_numeros + 1
        else:
            cont_simbolos = cont_simbolos + 1

    # Si la contrasenia no reune las condiciones salgo de la funcion devolviendo False
    if cont_caracteres < 6:
        return False
    elif cont_minusculas < 2:
        return False
    elif cont_mayuscualas < 1:
        return False
    elif cont_numeros < 2:
        return False
    elif cont_simbolos < 1:
        return False
    else:
        return True


# BACKEND
def listar_emails(texto):
    """
    Funcion que obtiene los emails de un texto
    :param texto: str texto con emails
    :return: list de emails
    """
    lista = []  # Se almacenar los emails con los errores de espacios y demás
    nueva_lista = []  # Se almacenaran los emails sin los espacios

    for renglon in texto:  # Guardo en una lista todos los correos
        lista.extend(renglon.split(sep=','))

    for i in lista:  # Sanitizo los correos
        copia = i.strip()
        copia1 = copia.rstrip()
        i = copia1
        if len(i) > 2:  # de esta forma no agrego a la lista los espacios en blanco
            nueva_lista.append(i)

    return nueva_lista


# BACKEND
def validar_emails(email):
    """
    Funcion que recibe un email y solo devuelve el email que reune ciertas condiciones
    :param email: str con formato "nombre@dominio.com"
    :return: str valido y corregido en caso de ser necesario o FALSE si el email no es valido
    """

    # Primero se construyen listas separndo el nombre, del dominio y del tipo.
    global condicion3
    lista_nombre_dominio = email.split(sep='@')  # ['nombre','dominio']
    lista_dominio_tipo = lista_nombre_dominio[1].split(sep='.')  # ['dominio','tipo','etc']

    # Condicion1 - Solo emails con dominio terminado en com, com.ar y org
    if lista_dominio_tipo[-1] == "ar" or lista_dominio_tipo[-1] == "com" or lista_dominio_tipo[-1] == "org":
        condicion1 = True
    else:
        return False

    # Condicion2 - Dominios "gmail.com" admiten nombres con puntuacion pero deben corregirse
    if lista_nombre_dominio[1] == "gmail.com":
        nombre = lista_nombre_dominio[0].replace('.', '')  # Aquí se eliminan los puntos del nombre
        lista_nombre_dominio[0] = nombre

        # Condicion3 - Dominios "dominios.org" no deben contener numeros
    if lista_dominio_tipo[-1] == "org":
        for i in lista_dominio_tipo[0]:
            if i.isdigit():
                return False
            else:
                condicion3 = True

    if condicion1 == True and lista_dominio_tipo[-1] != "org":
        nuevo_email = lista_nombre_dominio[0] + "@" + lista_nombre_dominio[1]
    elif condicion3 == True:
        nuevo_email = lista_nombre_dominio[0] + "@" + lista_nombre_dominio[1]

    return nuevo_email


# BACKEND

def tupla_a_listas(tupla):
    """
    La funcion recibe una tupla y devuelve dos listas ordenadas
    :param tupla: de longitud arbitraria
    :return: tupla con dos listas
    """
    # si la tupla tiene menos de 4 elementos por requerimiento debo disparar una excepcion
    try:
        if len(tupla) < 4:
            raise
    except:
        print("Se debe invocar con mas de 4 elementos")
    else:
        # listas a retornar
        lista1 = []
        lista2 = []
        # ordeno la lista formada por el parametro tupla
        lista = list(tupla)
        lista.sort()

        # construyo las dos listas "EL PATRON CREO QUE ES ASI"

        for i in range(1, ceil(len(lista) / 2) + 1):
            lista1.append(lista.pop(0))

        for i in range(1, len(lista) + 1):
            lista2.append(lista.pop(0))

        return (lista1, lista2)


# BACKEND
def cadena_a_enteros(texto):
    """
    Funcion que retorno todas las palabras de un texto que corresponden a valores númericos
    :param texto: str texto
    :return: list numeros enteros
    """

    lista = texto.split(sep=' ')  # Separa los palabras del texto y las guardo en una lista
    lista_nueva = []

    for i in lista:
        copia = i.strip(' .\n')  # Elimino los espacios en blanco y saltos de linea al inicio y final de palabras
        copia1 = copia.lstrip('0')  # Elimino los ceros a la izquierda de los numeros
        i = copia1
        if i.isdigit() == True:  # Si es digito lo agrego en la lista nueva
            lista_nueva.append(i)

    return lista_nueva
