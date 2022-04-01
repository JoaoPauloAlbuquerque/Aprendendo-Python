# Crie um programa que leia uma frase qualquer e diga se ela é
# um palíndromo, desconsiderandos os espaços.

s = str(input('Digite uma frase: ')).strip().upper()
p = s.replace(' ', '')
r = p[::-1]
if p == r:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
