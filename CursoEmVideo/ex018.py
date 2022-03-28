# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e
# e tangente desse ângulo.

import math

n = float(input('Digite um ângulo: '))
print(f'Seno: {math.sin(n)}')
print(f'Cosseno: {math.cos(n)}')
print(f'Tangente: {math.tan(n)}')
