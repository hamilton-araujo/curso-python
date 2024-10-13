# Questão 1

numero_str = input("Digite um número e eu direi se é impar ou par: ")

try:
    numero_int = int(numero_str)

    if numero_int % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
except:
    print("Você digitou um valor inválido")

# Questão 2

hora = input("Em que hora do dia estamos? ")

try:
    hora_int = int(hora)

    bomdia = hora_int <= 11
    boatarde = 12 <= hora_int <= 17
    boanoite = 18 <= hora_int <= 23

    if bomdia:
        print("Bom dia!")
    elif boatarde:
        print("Boa tarde!")
    elif boanoite:
        print("Boa noite!")
except:
    
    print("Você digitou um valor inválido")

# Questão 3

nome = input("Qual o seu nome? ")
tamanho_nome = len(nome)

nome_curto = tamanho_nome <= 4
nome_normal = 5 <= tamanho_nome <= 6
nome_longo = tamanho_nome > 6

if nome_curto:
    print(f"{nome}, seu nome é muito curto")
elif nome_normal:
    print(f"{nome}, seu nome é normal")
elif nome_longo:
    print(f"{nome}, seu nome é muito longo")