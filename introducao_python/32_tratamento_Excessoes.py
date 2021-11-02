n1 = int(input("Digite o número n1:"))
n2 = int(input("Digite o número n2:"))

"""try:
    print(n1/n2)
except:
    print("não consegui")
finally:
    print("Beleza, finalizado")"""


"""try:
    x = int(input("Digite um número: "))
    print(5/x)
except ValueError:
    print("Digite um número inteiro")
except ZeroDivisionError:
    print("Não digite 0")"""

try:
    x = int(input("Digite um número: "))
    print(5 / x)
except Exception as e:
    print(e)
