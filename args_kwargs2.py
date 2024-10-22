# *args aplica uma lista nos parâmetros de uma função

def test(arg, *args):
    print(f"O primeiro argumento é {arg}")
    for arg in args:
        print(f"Outro argumento: {arg}")

test("Primeiro argumento", "Segundo argumento", "Terceiro argumento")

# Questão 2

lista = ["segundo arg", "terceiro arg", "quarto arg", "quinto arg"]
test("primeiro argumento", *lista)

# Questão 3

# **kwargs aplica um dicionário nos parâmetros de uma função

def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

test_kwargs(nome="João", idade=25, cidade="São Paulo")