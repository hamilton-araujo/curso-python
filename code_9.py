def velocidade(espaco, tempo):
    velocidade = espaco/tempo
    return velocidade

print(f"Essa é a velocidade {velocidade(3,4)}")

def print_velocidade(espaco, tempo):
    velocidade = espaco/tempo
    print(f"Velocidade: {velocidade}")

print_velocidade(8,2)