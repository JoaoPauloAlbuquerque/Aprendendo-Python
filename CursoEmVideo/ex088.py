# Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint as rd
from time import sleep
jogos = list()
qtdjogo = int(input('Quantos jogos deseja sortear? '))
for i in range(0, qtdjogo):
    lista = list()
    while not len(lista) == 6:
        n = rd(1, 60)
        if n not in lista:
            lista.append(n)
    lista.sort()
    jogos.append(lista[:])
    print(f'Jogo {i + 1}: {jogos[i]}')
    lista.clear()
    sleep(1)
