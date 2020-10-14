from mis_funciones.mis_funciones import tupla_a_listas

tupla = (5, 3, 6, 10, 455, 12, 70, 8, 9, 110)
tupla1 = ('an', 'b', '3', 'dc', 'g')

print(f"Para la tupla {tupla} el valor retornado por la funcion es: ")
print(tupla_a_listas(tupla))  # cumplo con el requerimiento de mostrar dos listas ordenadas (elementos int)

print(f"\nPara la tupla {tupla1} el valor retornado por la funcion es: ")
print(tupla_a_listas(tupla1))  # cumplo con el requerimiento de mostrar dos listas ordenadas (elementos str)
