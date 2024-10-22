import random
import numpy as np

nove_digitos = str(random.randrange(100000000, 999999999))

valores_multiplicados = []

for i in range(len(nove_digitos)):
    multiplicados = (10 - i)*int(nove_digitos[i])
    valores_multiplicados.append(multiplicados)

soma = 10*np.sum(valores_multiplicados)
resto = soma % 11

digito1 = 0 if resto > 9 else resto
novo_cpf = nove_digitos + str(digito1)

valores_multiplicados1 = []

for i in range(len(novo_cpf)):
    multiplicados = (11 - i)*int(novo_cpf[i])
    valores_multiplicados1.append(multiplicados)

soma1 = 10*np.sum(valores_multiplicados1)
resto1 = soma1 % 11

digito2 = 0 if resto1 > 9 else resto1
cpf_final = novo_cpf + str(digito2)

print("Nove dígitos: {}; Dígito 1: {}; Dígito 2: {}; CPF: {}".format(nove_digitos, digito1, digito2, cpf_final))