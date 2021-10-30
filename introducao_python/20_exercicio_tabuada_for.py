# Receba um número e mostra a tabuada completa dele usando for
n1 = int(input("Digite um número: "))

print(f"Tabuada do {n1} ")
for i in range(0,11):
    print(f"{n1} x {i} = {n1 * i}")