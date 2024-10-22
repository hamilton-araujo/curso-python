pessoa = {"nome" : "João", "idade" : 25, "cidade" : "São Paulo"}

print(pessoa["nome"])

#mostrar chaves de um dicionario

print(pessoa.keys())

#mostrar valores de um dicionario

print(pessoa.values())

#podemos ter tuplas como chaves(n podemos ter listas como chaves)

dic = {(1,2,3) : "valor"}
print(dic.keys())

a = dict(um = 1, carro = "toyota", dois = True)
print(a)

