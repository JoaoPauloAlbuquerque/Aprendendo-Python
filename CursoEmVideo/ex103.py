# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado
# não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: '))
gol = int(g if g.isnumeric() else 0)

if gol >= 0 and n != '':
    ficha(n, gol)
elif gol >= 0 and n == '':
    ficha(gols=gol)
elif not(gol >= 0) and n != '':
    ficha(nome=n)
else:
    ficha()
