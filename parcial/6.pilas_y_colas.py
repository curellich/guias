"""
Puedo construir una COLA usando la libreria from collections import deque
o
Puedo construir una COLA trabajando con list()
"""

from collections import deque

# defino COLA con la libreria
cola = deque()
# defino la COLA sin la libreria
cola_sin_libreria = list()

# Con .append ingresan al final
for i in range(1, 5 + 1):  # pusheo elementos en la COLA de la misma forma con o sin libreria
    cola.append(f"platos {i}")
    cola_sin_libreria.append(f"platos {i}")

for i in range(1, 5 + 1):  # popeo elementos en la COLA de la misma forma con o sin libreria
    print(cola.popleft())  # Uso .popleft() para quitar el primer elemento de la cola
    print(cola_sin_libreria.pop(0))  # Uso .pop(0) para quitar siempre el primer elemento




