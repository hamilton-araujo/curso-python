import numpy as np
def coletar_cpf_verificar_formatacao(cpf, verifica):
    if len(cpf) == 14:
        print("CPF válido!")
        verifica = True
    elif len(cpf) < 14:
        print("CPF inválido.")
        verifica = False
    elif len(cpf_digitado) > 14:
        print("CPF inválido.")
        verifica = False
    elif cpf_digitado[3] != ".":
        print("CPF inválido.")
        verifica = False
    elif cpf_digitado[8] != ".":
        print("CPF inválido.")
        verificar = False
    elif cpf_digitado[12] != "-":
        print("CPF inválido.")
        verifica = False

verificador = True

while verificador:

    cpf_digitado = input("Digite o seu CPF(Com pontos e traços): ")
    coletar_cpf_verificar_formatacao(cpf_digitado, verificador)
    if verificador == True:
        break
    else:
        continue

cpf_sem_pontos = cpf_digitado.replace(".", "").replace("-", "")

# cpf_sem_pontos_sem_digitos = cpf_sem_pontos.replace(cpf_sem_pontos[-2], "").replace(cpf_sem_pontos[-1], "")

# #tratar os dados do cpf para fazer o cálculo do primeiro digito
# valores_multiplicados = []

# for numero in cpf_sem_pontos_sem_digitos:
#     multiplicados = (10 - int(numero))*cpf_sem_pontos_sem_digitos[int(numero)]
#     valores_multiplicados.append(multiplicados)

# soma_multiplicados = np.sum(valores_multiplicados)
# soma_multiplicados = soma_multiplicados*10
# #calculando o resto da multiplicação

# resto = soma_multiplicados % 11

# digito1 = 0 if resto > 9 else resto

# if digito1 == cpf_sem_pontos[10]:
#     print("Primeiro dígito verificado com sucesso!")
# else:
#     print("Primeiro dígito inválido!")

# #tratar os dados do cpf para fazer o cálculo do segundo digito

# digito1_str = str(digito1)

# cpf_sem_pontos_sem_digitos1 = cpf_sem_pontos_sem_digitos + digito1_str

# valores_multiplicados1 = []

# for numero in cpf_sem_pontos_sem_digitos1:
#     multiplicados1 = (11 - numero)*cpf_sem_pontos_sem_digitos1[numero]
#     valores_multiplicados1.append(multiplicados1)

# soma_multiplicados1 = np.sum(valores_multiplicados1)
# soma_multiplicados1 = soma_multiplicados1*10

# resto1 = soma_multiplicados1 % 11

# digito2 = 0 if resto1 > 9 else resto1

# if digito2 == cpf_sem_pontos[11]:
#     print("Segundo dígito verificado com sucesso!")
# else:
#     print("Segundo dígito inválido!")

print(cpf_sem_pontos)
nove_digitos = cpf_sem_pontos[:9]

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

print(nove_digitos, digito1, digito2, cpf_sem_pontos, cpf_final)

if cpf_final == cpf_sem_pontos:
    print("CPF verificado com sucesso!")
else:
    print("CPF inválido!")