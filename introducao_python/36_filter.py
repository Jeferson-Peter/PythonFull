x = [12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# x = [{"nome": "caio", "idade": 20}]

# x = list(filter(lambda x: x['idade'] <= 20 , x ))
# x = list(filter(lambda x: x['nome'] == 'caio', x )) , x ))
x = list(filter(lambda x: x < 18 or x % 2 ==0, x ))
print(x)