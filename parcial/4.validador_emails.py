from mis_funciones.mis_funciones import validar_emails
from mis_funciones.mis_funciones import listar_emails

lista_emails_validados = []
nombre_archivo = "./mis_funciones/emails.txt"

# Manejo de exepcion: FileNotFoundError
try:
    with open(nombre_archivo) as f:
        texto = open(nombre_archivo, "rt")

except FileNotFoundError:
    print(f"El nombre del archivo {nombre_archivo} no existe ")
else:
    lista_emails = listar_emails(texto)  # obtengo una lista de emails a partir del archivo

    for i in lista_emails:  # valido los emails y creo la lista con los emails que cumplen las condiciones
        email_comprobado = validar_emails(i)
        if email_comprobado != False:
            lista_emails_validados.append(email_comprobado)

    print(set(lista_emails_validados))  # muestro por pantalla la lista sin los correos repetidos
