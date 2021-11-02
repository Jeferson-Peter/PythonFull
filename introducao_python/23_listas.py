idades = [ 3, 32, 5, 50, 2]

# for i in range(0, len(idades)):
#     print(idades[i], i)
#
# for i in idades:
#     print(i)

x = list(enumerate(idades))
print(x)

for i, j in enumerate(idades):
    print(f"i={i}, j={j}")

idades_pares = []
for i in idades:
    if i % 2 == 0:
        idades_pares.append(i)
print(idades_pares)


