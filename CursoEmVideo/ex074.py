# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint as rd
lista = (rd(0, 100), rd(0, 100), rd(0, 100), rd(0, 100), rd(0, 100))
print('Os números sorteador foram: ', end='')
for n in lista:
    print(n, end=' ')
print(f'\nMaior valor: {max(lista)}')
print(f'Menor valor: {min(lista)}')
