# Recebe um número e mostre todos os números pares de 0 até o número digitado
n = int(input("Digite um número: "))

i = 1
while i <= n:
    if i % 2 ==0:
        print (i)

    i += 1