#Escreva um programa que receba notas de uma aluno (0 - 10), caso
# Anota digitada esteja fora desse intervalo peça para o professor digitar novamente

while True:
    nota = int(input("Digite a nota do aluno: "))
    if nota >= 0 and nota <= 10:
        print(f"Nota {nota} registrada com sucesso")
        break

    print("Nota inválida digite novamente")