# Crie um programa que leia um número real qualquer
# pelo teclado e mostre na tela a sua porção inteira.

import math
n = float(input('Digite um número com ponto flutuante: '))
print(f'Parte inteira: {math.trunc(n)}')
