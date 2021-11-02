import lista as lista
from pympler.asizeof  import asizesof

# print(asizesof(5))
# print(asizesof('s'))
#
# def dobro(lista):
#     lista_dobro = []
#     for i in lista:
#         lista_dobro.append(i*2)
#     yield lista_dobro
#
# y = asizesof(dobro(range(0,100)))
#
# print(y)

def dobro(lista):
    for i in lista:
        yield i
        # while True:
        #     i+=1
        #     yield i


def dobro2(lista):
    lista_2 = []
    for i in lista:
        lista_2.append(i)
    return lista_2
        # while True:
        #     i+=1
        #     yield i

x = dobro(range(0,10000))
y = dobro2(range(0,10000))
print(asizesof(x))
print(next(x))
print(next(x))
print(next(x))

print(asizesof(y))

# while True:
#     try:
#         print(next(x))
#     except StopIteration:
#         break

for i in x:
    print(i)