import random

num_cajas = 3
filas = [[] for _ in range(num_cajas)]

for i in range(10):
    cliente = "Cliente " + str(i+1)
    fila_corta = min(filas, key=len)
    fila_corta.append(cliente)

for i, fila in enumerate(filas):
    print("Caja", i+1, ":", len(fila), "clientes:", fila)