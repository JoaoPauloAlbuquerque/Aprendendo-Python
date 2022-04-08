# Crie um programa que gerencia o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonado.

jogador = dict()
gols = list()
nome = str(input('Qual o nome do jogador: '))
qtd_partidas = int(input(f'Quantas partidas {nome} jogou? '))
for i in range(0, qtd_partidas):
    gol = int(input(f'Quantos gols na partida {i + 1}: '))
    gols.append(gol)
jogador['nome'] = nome
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for p, i in enumerate(jogador['gols']):
    print(f'    => Na partida {p + 1}, fez {i} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
