lista = (
    'hamburguer',
    'suco',
    'pizza',
    'pudin'
)
print(lista[::-1])

print('-' * 30)
for comida in lista:
    print(f'{comida}')

print('-' * 30)
# Se não quizer usar o for com range()
# Da pra usar o enumerate() para pegar a posição da lista
for posicao, comida in enumerate(lista):
    print(f'{comida} na posição {posicao}')

print('-' * 30)
# Ordenar uma lista
print(sorted(lista))

print('-' * 30)
# juntando listas
a = (8, 2, 3, 4)
b = (5, 6, 7, 8)
c = a + b
d = b + a
print(f'Lista a: {a}')
print(f'Lista b: {b}')
print(f'Lista a + b: {c}')
print(f'Lista b + a: {d}')

print('-' * 30)
# pegar a posição de um ítem na lista
print(f'O 8 está no index: {d.index(8)} da lista b + a')
# Pegar um index a partir de uma posição
# O primeiro parâmetro é o ítem que está procurando, e o segundo e a partir de qual posição
print(f'Na lista a + b, a partir da posição 1, o 8 está posição {c.index(8, 1)}')

print('-' * 30)
# Deletando toda a tupla
pessoa = ('João Paulo', 20, 'M')
del pessoa
