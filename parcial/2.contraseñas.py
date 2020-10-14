from mis_funciones import mis_funciones

# FRONTEND
contrasenia = input('Ingrese clave: ') #no es necesario hacer manejo de excepciones, puesto que TODA entrada es clave

# Compruebo si la contrasenia reune los requisitos
if mis_funciones.validar_contrasenia(contrasenia) != True:
    print(f"La contraseña {contrasenia} no reune los requisitos ")
else:
    print(f"La contraseña {contrasenia} es segura ")
