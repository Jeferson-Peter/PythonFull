idades = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]
    ]
print(idades[2][3])
print("antes for")
for i in range(0, len(idades)):
    print(i)
    for j in range(0, len(idades[i])):
        print(idades[i][j])