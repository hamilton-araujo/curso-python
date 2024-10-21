def soma(a, b):
    soma = a + b
    print(soma)

def subtracao(a, b):
    subtracao = a - b
    print(subtracao)

def calculacao(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a*b
    divisao = a/b if b!=0 else "Divisão por zero não é permitida."
    print(f"Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}, Divisão: {divisao}")

soma(1,2)
subtracao(8,4)
calculacao(5,2)