def funcao():
    print("oi")
    print("função")

funcao()

def soma_numero(*args): # lista
    print(f" args = {args} ")
    soma = 0
    for i in args:
        soma += i
    return soma

soma_numero(1,2,3,4,5,6,7,8,9)

def teste(**kwargs):# dicionário
    print(kwargs.get("teste1"))
    print(f" args = {kwargs} ")
# False e None sao falsos


teste(teste1 = 1, teste2 = 4)