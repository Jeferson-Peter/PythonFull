#Escreva um programa onde o usuário digite duas notas e ele mostre a mmédia das duas notas
"""Minha Solução"""
i = 1
soma = 0
while i <= 2:
    nota = float(input(f"Digite a sua nota {i}: "))
    soma = soma + nota
    i= i + 1

media = soma / 2

print(f"Sua média é {media}")
"""Minha Solução"""

"""Solução Caio"""
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

print(f"Sua média é {media}")

"""Solução Caio"""