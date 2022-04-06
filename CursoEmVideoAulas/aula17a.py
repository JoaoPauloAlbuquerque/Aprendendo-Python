# Criando uma lista
lista = ['Hamburguer', 'Pizza', 'Suco', 'Picolé']

# Adicionando ítens no final da lista
lista.append('Cachorro quente')

# Inserindo ítens numa posição expecífica da lista
lista.insert(0, 'Café')

# Deletando um ítem expecífico na lista
del lista[2]
lista.pop(3)
lista.remove('Hamburguer')

# Deletando o último ítem da lista
lista.pop()

# Criando uma lista com o range()
# Neste caso, ele vai criar uma lista com os valores de 4 até 10
valores = list(range(4, 11))

# Ordenando uma lista na ordem crescente
ordem = [8, 3, 4, 1, 9, 10]
print(ordem.sort())

# Ordenando uma lista na ordem decrescente
ordem.sort(reverse=True)
