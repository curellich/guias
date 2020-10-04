def cuenta_caracteres(nombre):
    # Diccionario para retornar los valores
    dicc = {'l_mayusc': '', 'l_minusc': '', 'otros': ''}
    # Estos son los 3 contadores
    letras_mayusculas = 0
    letras_minusculas = 0
    otros_caraceres = 0

    fichero = open(f'{nombre}', 'r')
    # Recorro el archivo identificando los caracteres por alfabeticos(mayusc y minusc) y no alfabeticos

    caracter = fichero.read(1)
    while caracter != '':
        if caracter.isupper() == True:
            letras_mayusculas += 1
            caracter = fichero.read(1)
        elif caracter.islower() == True:
            letras_minusculas += 1
            caracter = fichero.read(1)
        else:
            otros_caraceres += 1
            caracter = fichero.read(1)

    dicc['l_mayusc']=letras_mayusculas
    dicc['l_minusc']=letras_minusculas
    dicc['otros'] = otros_caraceres

    fichero.close()

    return diccw

