# Faça um programa que o usuário possa cadastrar n pessoas,
# armazanando seu nome, idade e altura
pessoas = []
while True:
    decisao = int(input("Digite 1 para cadastrar uma pessoa e 2 para sair: "))
    if decisao == 2:
        break
    # nome = input("Digite o nome da pessoa: ")
    # idade = int(input("Digite a idade:"))
    # altura = float(input("Digite a altura: "))
    # pessoa = {"nome": nome, "idade": idade, "altura": altura}
    pessoa = {"nome": input("Digite o nome da pessoa: "),
              "idade":int(input("Digite a idade:")),
              "altura": float(input("Digite a altura: "))}
    pessoas.append(pessoa)
print(pessoas)