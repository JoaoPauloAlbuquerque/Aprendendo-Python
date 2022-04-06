# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados;
# A soma dos valores da terceira coluna;
# O maior valor da segunda coluna;

matriz = [[], [], []]
for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
        n = int(input(f'Digite o valor [{i}, {j}]: '))
        matriz[i].append(n)
for i in matriz:
    for j in i:
        print(f'[ {j} ]', end=' ')
    print()

somapar = 0
somaterceiracoluna = 0
maiorsegundalinha = 0
for linha, i in enumerate(matriz):
    for coluna, j in enumerate(i):
        if j % 2 == 0:
            somapar += j
        if coluna == 2:
            somaterceiracoluna += j
        if linha == 1:
            if maiorsegundalinha == 0:
                maiorsegundalinha = j
            else:
                if maiorsegundalinha < j:
                    maiorsegundalinha = j
print(f'A soma de todos os valores par é {somapar}')
print(f'A soma dos valores da terceira coluna é {somaterceiracoluna}')
print(f'O maior da segunda linha é {maiorsegundalinha}')
