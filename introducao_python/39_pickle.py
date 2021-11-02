import pickle
class Pessoa:
    name = 'Pessoa'
    idade = 20

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoas('jeferson', 20)
x = [1,2,3,4]

arq = open('arquivo.pkl', 'wb' )
pickle.dump( x, arq)
# pickle.dump( Pessoa, arq)

arq = open('arquivo.pkl', 'rb' )
retornou = pickle.load(arq)

print(retornou)
# print(retornou.nome)


with open('arquivo.pkl', 'wb') as f:
    pickle.dump(f, p1)
