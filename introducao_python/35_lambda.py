
def teste():
    return lambda *idade: print(idade)

x = teste()
x('jeferson', "Marcos")
print(x)