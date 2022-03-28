# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e
# e tangente desse ângulo.

from math import sin, cos, tan, radians

n = float(input('Digite um ângulo: '))
print(f'Seno: {sin(radians(n)):.2f}')
print(f'Cosseno: {cos(radians(n)):.2f}')
print(f'Tangente: {tan(radians(n)):.2f}')
