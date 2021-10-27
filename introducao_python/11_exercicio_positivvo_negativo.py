# Recceba um Número e exiba  se ele é  positivo ou negativo

n = float(input("Digite um número qualquer:"))

if n < 0:
    print(f"O Número {n} é menor que zero")
elif n > 0 :
    print(f"O Número {n} é maior que zero")
else:
    print("O número é 0")