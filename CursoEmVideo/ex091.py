# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados num dicionário. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor o maior número no dado.

from random import randint as rd
from time import sleep
from operator import itemgetter
# j = dict()
# j['jogador1'] = rd(1, 6)
# j['jogador2'] = rd(1, 6)
# j['jogador3'] = rd(1, 6)
# j['jogador4'] = rd(1, 6)
# print('Valores sorteados:')
# for k, v in j.items():
#     print(f'    O {k} tirou {v}')
#     sleep(1)
# lista = list()
# count = 0
# for k, v in j.items():
#     if count == 0:
#         lista.append([k, v])
#         count += 1
#     else:
#         if v > lista[-1][1]:
#             lista.append([k, v])
#         else:
#             for p, i in enumerate(lista):
#                 if v <= i[1]:
#                     lista.insert(p, [k, v])
#                     break
# j.clear()
# for i in range(len(lista) - 1, -1, -1):
#     j[lista[i][0]] = lista[i][1]
# print('Ranking dos jogadores:')
# count = 1
# for k, v in j.items():
#     print(f'    {count}º lugar: {k} com {v}')
#     count += 1


# VERSÃO DO GUANABARA
jogo = {'jogador1': rd(1, 6),
        'jogador2': rd(1, 6),
        'jogador3': rd(1, 6),
        'jogador4': rd(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# Ordenar os itens do dicionário:
# No método "sorted(itens_do_dicionário, itemgetter() - 0 para organizar por chave, 1 para organizar por valor)"
# O método sort() retorna uma lista
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKINK DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

