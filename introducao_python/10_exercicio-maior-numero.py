#Receba  3 números inteiros e exiba o maior deles

n1 = int(input("Digite o primeiro valor intero: "))
n2 = int(input("Digite o segundo valor intero: "))
n3 = int(input("Digite o terceiro valor intero: "))

if n1 >  n2 and n1 > n3:
    print(f"O valor de n1 {n1} é maior")
elif  n2 > n1 and n2 > n3:
    print(f"O valor de n2 {n2} é maior")
elif n3 > n2  and n3 > n1:
    print(f"O valor de n3 {n3} é maior")
    """Solução de ambos"""
