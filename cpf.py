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

#tratar os dados do cpf para fazer o cálculo do primeiro digito
valores_multiplicados = []

for numero in cpf_sem_pontos:
    multiplicados = (10 - numero)*cpf_sem_pontos[numero]
    valores_multiplicados.append(multiplicados)

soma_multiplicados = np.sum(valores_multiplicados)
soma_multiplicados = soma_multiplicados*10
#calculando o resto da multiplicação

resto = soma_multiplicados % 11

digito1 = 0 if resto > 9 else resto

if digito1 == cpf_sem_pontos[10]:
    print("Primeiro dígito verificado com sucesso!")
else:
    print("Primeiro dígito inválido!")

#tratar os dados do cpf para fazer o cálculo do segundo digito

