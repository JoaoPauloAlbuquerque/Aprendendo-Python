# Melhore o jogo do desafio 028, onde o computador vai "pensar" em um número entre 0 e 10.
# Porém, agora o jogador vai tentar adivinhar até acertar, mostrando no
# final quantos papites foram necessários para vencer.

from random import randint
from time import sleep
count = 0
r = randint(0, 10)
while True:
    print('=-' * 30)
    n = int(input('Digite um número inteiro entre 0 e 10: '))
    count += 1
    print('PROCESSANDO...')
    sleep(2)
    if n < r:
        print(f'\033[31mVocê errou!\033[m o número é um pouco maior...')
    elif n > r:
        print(f'\033[31mVocê errou!\033[m o número é um pouco menor...')
    else:
        print('\033[32mVocê acertou!\033[m')
        break
print(f'Você precisou de {count} tentativas para acertar')
