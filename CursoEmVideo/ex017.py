# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo,
# calcule e mostre a o comprimento da hipotenusa.

from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print(f'Hipotenusa vale: {hypot(ca, co):.2f}')
