# Crie um programa que faça o computador jogar jokenpô com você.

from random import choice
from time import sleep
o = [
    'pedra',
    'papel',
    'tesoura'
]

print('=' * 40)
print(f'Oções: {o}')
print('=' * 40)
s = str(input('Escolha: '))
e = choice(o)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if e == o[2] and s == o[0]:
    print(f'computador: {e}')
    print('Você ganhou!')
elif e == o[0] and s == o[1]:
    print(f'Computador: {e}')
    print('Você ganhou!')
elif e == o[1] and s == o[2]:
    print(f'Computador: {e}')
    print('Você ganhou!')
elif e == s:
    print(f'Computador: {e}')
    print('Empatou!')
else:
    print(f'Computador: {e}')
    print('Você perdeu!')
