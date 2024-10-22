# Questão 1

def teste_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

args = ("um", 2, 3, 4)
teste_args_kwargs(*args)

kwargs = dict(arg3 = 3, arg2 = "dois", arg1 = "um", arg4 = "quatro")
teste_args_kwargs(**kwargs)