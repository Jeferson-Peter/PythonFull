# Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou gual que 6)
# Se ele ficou de recuperação (nota maior ou igual a 4) ou se ele foi
#  Reprovado (nota menor do  que 4)

qtde_notas = 4
i = 1
soma = 0

while i <= qtde_notas:
    nota = float(input(f"Digite a nota {i}: "))
    soma = soma + nota
    i = i + 1

media = soma / qtde_notas

if media >= 6:
    print(f"A sua média é {media}. Você foi aprovado")
elif media >= 4:
    print(f"A sua média é {media}. Você está de recuperação")
else:
    print(f"A sua média é {media}. Você está reprovado")


