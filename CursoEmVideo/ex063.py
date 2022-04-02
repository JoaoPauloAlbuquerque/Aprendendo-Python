# Escreva um programa que leia um número n inteiro qualquer e mostre na tela
# os 'n' primeiros elementos de uma sequência de fibonacci.

n = int(input('Digite uma quantidade para mostrar a sequencia de fibonacci: '))
i = 0
ant1 = 1
ant2 = 0
print('0 - 1 - ', end='')
while i < (n - 2):
    p = ant1 + ant2
    ant2 = ant1
    ant1 = p
    print(f'{p} - ', end='')
    i += 1
