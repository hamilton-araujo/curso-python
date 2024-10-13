numero_str = input("Vou dobrar o número que você digitar: ")

try:
    print("STRING:", numero_str)
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print(f"O dobro de {numero_float} é {2*numero_float}")
except:
    print("Insira um número válido")
