# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# Qual é o total gasto;
# Quantos produtos custam mais de R$1000,00;
# Qual é o nome do produto mais barato;

totalgasto = 0
produtoscaros = 0
maisbaratopreco = 0
maisbaratonome = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    if totalgasto == 0:
        maisbaratonome = nome
        maisbaratopreco = preco
    if maisbaratopreco > preco:
        maisbarato = nome
        maisbaratopreco = preco
    totalgasto += preco
    if preco > 1000:
        produtoscaros += 1
    saida = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
print(f'Total gasto: R${totalgasto}')
print(f'Produtos acima de R$1000,00: {produtoscaros} produtos')
print(f'Produto mais barato: {maisbaratonome}')
