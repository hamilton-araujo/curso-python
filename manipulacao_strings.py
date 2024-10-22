# # métodos para tratar strings

# # split e join com string e lista
# # split - divide uma string
# #join - une uma string

# frase = "Eu amo Python, entendeu? "
# lista_frase = frase.split(",")

# for i, frase in enumerate(lista_frase):
#     print(lista_frase[i])

# #strip é um método para tirar os espaços do final e do começo
# for i, frase in enumerate(lista_frase):
#     print(lista_frase[i].strip())

frase = "        olha só que         ,     coisa legal     "
lista_frases_cruas = frase.split(",")

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

# usando o join

frases_unidas = ", ".join(lista_frases)
print(frases_unidas)