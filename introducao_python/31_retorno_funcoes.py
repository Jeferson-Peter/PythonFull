def soma(n1, n2):
    return n1 + n2

y = soma(1,2)
print(y)

"""Compactação em return"""

def soma_compacta(n1, n2):
    return n1 + n2, n1, n2

z = soma_compacta(1,2)
a, b, c = soma_compacta(1,2)
print(z)
print(a, b, c)
"""Compactação em return"""