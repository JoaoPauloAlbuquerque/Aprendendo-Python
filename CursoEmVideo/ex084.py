# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# Quantas pessoas foram cadastradas;
# Uma listagem com todas as pessoas mais pesadas;
# Uma listagem com todas as pessoas mais leves;

pessoas = list()
dados = list()
while True:
    dados.append(str(input('Digite seu nome: ')).strip())
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    saida = str(input('Deseja continuar? [S/N] '))
    if saida in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
maior = list()
menor = list()
for p in pessoas:
    if len(maior) == 0:
        maior.append(p[:])
        menor.append(p[:])
    else:
        if maior[0][1] == p[1]:
            maior.append(p[:])
        elif maior[0][1] < p[1]:
            maior.clear()
            maior.append(p[:])
        if menor[0][1] == p[1]:
            menor.append(p[:])
        elif menor[0][1] > p[1]:
            menor.clear()
            menor.append(p[:])
print(f'O maior peso foi de {maior[0][1]}kg. Foram elas: ', end='')
for p in maior:
    print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor[0][1]}kg. Foram elas: ', end='')
for p in menor:
    print(f'[{p[0]}]', end=' ')
