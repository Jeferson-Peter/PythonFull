# x = [ i for i in range(12,26)]
x = [{"nome": "jefe", "idade":20}, {"nome": "caio", "idade":40}]
# x = list(map(lambda x: 10 if x < 30 else(x), x))
x = list(map(lambda x: {'nome': x['nome'], 'idade': 'menor que 30 anos'} if x['idade'] < 30 else(x), x))
print(x)