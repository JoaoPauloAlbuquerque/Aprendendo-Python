# Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite um número: '))
f = n
c = n - 1
while c > 0:
    f *= c
    c -= 1
print(f'O fatorial de {n} é {f}')
