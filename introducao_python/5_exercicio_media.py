#Escreva um programa onde o usuário digite duas notas e ele mostre a mmédia das duas notas
i = 1
soma = 0
while i <= 2:
    nota = float(input(f"Digite a sua nota {i}: "))
    soma = soma + nota
    i= i + 1

media = soma / 2

print(f"Sua média é {media}")