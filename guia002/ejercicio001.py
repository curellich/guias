"""
1- Se necesita un programa que lea un archivo de texto e imprima por pantalla la cantidad de letras mayúsculas,
minúsculas y otros caracteres que no sean letras.
TIPs: Recordar de las guías anteriores las funciones aplicadas sobre strings, en particular isupper() y islower()
que retornan True en caso de tratarse de caracteres en mayúsculas o minúsculas, respectivamente.
Resultado esperado: Si el archivo texto.txt contiene la siguiente frase:
"""



from ej1.mis_funciones import cuenta_caracteres
info_caracteres={}
nombre = 'texto.txt'
info_caracteres=cuenta_caracteres(nombre)

print(f"la cantidad de mayusculas es {info_caracteres['l_mayusc']}")
print(f"la cantidad de minusculas es {info_caracteres['l_minusc']}")
print(f"la cantidad de otros caracteres es {info_caracteres['otros']}")

