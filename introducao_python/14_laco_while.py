"""i = 0
while i < 5:
    print("Olá Tuudo bem?")
    print("Como você vai")
    i += 1"""

i = 0

while i < 10:
    print(i)
    if i % 2 == 1:
        i += 2
        continue
    # break
    i += 1