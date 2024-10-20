import numpy as np

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

maior_numero = 0
menor_numero = 10000

for i in range(len(lista)):
    if lista[i] > maior_numero:
        maior_numero = lista[i]
    
    if lista[i] < menor_numero:
        menor_numero = lista[i]

print(maior_numero, menor_numero)

numeros_pares = []

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        numeros_pares.append(lista[i])
    
print(numeros_pares)

print(lista.count(lista[0]))

print(np.mean(lista))

numeros_negativos = []

for i in range(len(lista)):
    if lista[i] < 0:
        numeros_negativos.append(lista[i])

print(np.sum(numeros_negativos))