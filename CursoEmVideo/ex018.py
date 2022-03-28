# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e
# e tangente desse ângulo.

import math

n = float(input('Digite um ângulo: '))
print(f'Seno: {math.sin(math.radians(n)):.2f}')
print(f'Cosseno: {math.cos(math.radians(n)):.2f}')
print(f'Tangente: {math.tan(math.radians(n)):.2f}')
