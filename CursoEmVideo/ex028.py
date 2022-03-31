# Escreva um programa que faça o computador "pensar" num número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.

from random import randint
from time import sleep
r = randint(0, 5)
n = int(input('Digite um número inteiro entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if r == n:
    print('Você acertou!')
else:
    print(f'Você errou! o número selecionado foi {r}')
