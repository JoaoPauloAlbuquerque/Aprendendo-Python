# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cor = {
    'none': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

numero = int(input('Digite um número inteiro: '))
situacao = f'{numero} NÃO É PRIMO'
posicoes = ''
count = 0
for c in range(1, numero + 1):
    if (numero % c) == 0:
        count += 1
        posicoes += f'{cor["vermelho"]}{c}{cor["none"]} '
    else:
        posicoes += f'{cor["verde"]}{c}{cor["none"]} '
if count == 2:
    situacao = f'{numero} É PRIMO!'
print(situacao)
print(f'{numero} foi divisível {count} vezes')
print(f'{numero} foi divisível por:')
print(posicoes)
