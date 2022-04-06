# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores ligos pelo teclado.
# No final, mosrte a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        n = int(input(f'Digite o valor [{i}, {j}]: '))
        matriz[i].append(n)
for i in matriz:
    for j in i:
        print(f'[ {j} ]', end=' ')
    print()
