# for i in range(0,50, 2):
#     print(i)
for i in range(100,0, -2):
    print(i)

x = input("Digite seu nome:")
for i in x:
    print(i)


# For aninhado
for i in range(0,3):
    for j in range(0,3):
        print(f"i = {i}, j = {j}")

k = 0
for i in range(0,10000):
    for i in range(0,10000):
        print(f"i = {i}, j = {j}")
        k +=1
print(k)