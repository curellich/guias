def fibonacci_recursiva(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return (fibonacci_recursiva(n - 1) + fibonacci_recursiva(n - 2))

def fibonacci_iterativa(n):
    if n == 0 or n == 1:
        return 0;
    ant2=0
    ant1=1

    for i in range(2,n+1):
        fibn=ant1+ant2
        ant2=ant1
        ant1=fibn
    return fibn


n = int(input("Ingrese un numero para calcular serie fibonacci\n"))
print(f"Recursiva- La serie fibonacci de {n} es {fibonacci_recursiva(n)}")
print(f"Iterativa- La serie fibonacci de {n} es {fibonacci_iterativa(n)}")
