# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveiamento de cada jogador.

jogadores = list()
jogador = dict()
gols = list()
tot_gols = 0
while True:
    nome = str(input('Qual o nome do jogador: '))
    qtd_partidas = int(input(f'Quantas partidas {nome} jogou? '))
    for i in range(0, qtd_partidas):
        gol = int(input(f'Quantos gols na partida {i + 1}: '))
        gols.append(gol)
        tot_gols += gol
    jogador['nome'] = nome
    jogador['gols'] = gols[:]
    jogador['total'] = tot_gols
    gols.clear()
    tot_gols = 0
    jogadores.append(jogador.copy())
    saida = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
print('-=' * 40)
print(f'{"No.":<5}{"Nome":<10}{"Gols":<20}{"Total":>5}')
print('-' * 40)
for p, v in enumerate(jogadores):
    print(f'{p:<5}{v["nome"]:<10}{str(v["gols"]):<20}{v["total"]:>5}')
while True:
    print('-' * 40)
    mostrar = int(input('Mostrar dados de qual jogador? '))
    if mostrar == 999:
        break
    if 0 <= mostrar < len(jogadores):
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar]["nome"]}:')
        for p, v in enumerate(jogadores[mostrar]["gols"]):
            print(f'   No jogo {p} fez {v} gols.')
    else:
        print(f'ERRO! Não existe jogador com o código {mostrar}! Tente novamente.')
