import os

lista = []

while True:
    selecionador = input("Selecione uma das opções:\n[i]nserir [r]emover [l]istar: ")

    if selecionador.lower() == 'i':
        os.system("clear")
        item = input("Digite o item que deseja inserir: ")
        lista.append(item)
        print(f"Item '{item}' inserido com sucesso.")
        continue
    elif selecionador.lower() == 'r':
        os.system("clear")
        item = input("Digite o item que deseja remover: ")
        if item in lista:
            lista.remove(item)
            print(f"Item '{item}' removido com sucesso.")
            continue
        else:
            print(f"Item '{item}' não encontrado na lista.")
            continue
    elif selecionador.lower() == 'l':
        os.system("clear")
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            print("Itens na lista:")
            for item in lista:
                print(item)
        continue
    else:
        os.system("clear")
        print("Opção inválida.")
        continue