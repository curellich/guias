def interes_recursivo(c,i,n):
    if n == 1:
        return c * (1+i)
    return interes_recursivo(c,i,n-1)
print(f"El capital compuesto para 3 meses es de 100 pesos a 10% de interes es: {interes_iterativo(100,0.1,3)}")
print(f"El capital compuesto para 3 meses es de 100 pesos a 10% de interes es: {interes_recursivo(100,0.1,3)}")

