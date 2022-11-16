# 2. Crea una archivo python que muestre 10 números aleatorios entre 1 y 100 y los muestre ordenados

import random
lista = []
for n in range(10):
    lista.append(random.randint(1,100))
lista.sort()
print(lista)