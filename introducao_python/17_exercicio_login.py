# Defina um usuário e senha e depois verifique se
# são válidos

USUARIO = "jeferson"
SENHA = "tesla model x"

while True:
    usuario = input("Digite o seu usuário: ")
    senha = input("Digite a senha do usuário: ")
    if USUARIO == usuario and SENHA == senha:
        print("Login Efetuado com sucesso")
        break

    print("Usuario ou senha inválidos, tente novamente")