# Receba um número inteiro do usuário e mostre a tabuada desse número.
number = int(input("Digite o número da tabuada que queira saber: "))

i = 0

print(f"\nTABUADA DO {number} ")
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
