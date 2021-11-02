# Escrever em arquivo
# arquivo = open('pessoas.txt',"w")
# arquivo.write("olá")
# Escrever em arquivo

# Adicionar em arquivo
# arquivo = open('pessoas.txt',"a")
# i=0
# while True:
#     if i > 5:
#         break
#     arquivo.write(input("Digite o nome da pessoa: ")+ "\n")
#     i+=1
# Adicionar em arquivo

# arquivo = open('pessoas.txt',"r")
# resultado = arquivo.readlines()
# x=[]
# for i in resultado:
#     x.append(i.split())
# print(resultado)
# print(x[1])
# arquivo.close()

with open('pessoas.txt','r') as arq:
    x = arq.read()
    print(x)