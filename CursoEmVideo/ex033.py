# Faça um programa que leia três números e mostre qual é o menor e qual é o maior.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior número é {maior}')
print(f'O menor núemro é {menor}')
