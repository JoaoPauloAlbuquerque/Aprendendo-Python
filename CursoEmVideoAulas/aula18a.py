lista = [['João Paulo', 20], ['Pedro', 19], ['Jose', 34], ['Maria', 30]]
print(lista[1])
print(lista[0][1])


galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Digite um nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
         