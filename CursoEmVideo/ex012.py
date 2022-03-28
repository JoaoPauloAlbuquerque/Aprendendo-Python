# Faça um algorítmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

n = float(input('Digite o preço do produto (R$): '))
print(f'O novo preço com desconto de 5% será de R${n - (n * 0.05)}')
