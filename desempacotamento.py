# desempacotamento em chamadas
#de métodos e funções

string = "ABCD"
lista = ["Maria", "Julia", 1, 2 , 3, (4,5,6), "Eduarda"]
tupla = "Python", "é", "legal"

# p, b, *_, ap, u = lista
# print(p,u,ap)

# for nome in lista:
#     print(nome, end = " ")

print("Maria", "Julia", 1, 2 , 3, "Eduarda")
print(*lista)
print(*string)
print(*tupla)
print("\n")
print(*lista, sep = "\n")