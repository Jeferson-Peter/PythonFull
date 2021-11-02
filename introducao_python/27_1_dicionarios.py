x = {"nomes":[], "idade":21}

x['nomes'].append("Jeferson Peter")
x['nomes'].append("Marco Aurelio")

print(x)
print(x['nomes'][0])

pessoas = [{"nome": "Jeferson", "idade":21},  {"nome": "Caio", "idade":21}]

for pessoa in pessoas:
    print(pessoa)
    print(pessoa['nome'])