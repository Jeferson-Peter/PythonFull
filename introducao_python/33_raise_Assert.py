# raise ValueError("Deu merda")

def soma (n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError("n1 e n2 não podem ser zero")
    return n1 + n2

print(soma(1,2))

x = 5
assert x  > 0, "Deu merda"