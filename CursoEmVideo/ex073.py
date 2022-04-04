# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato brasileiro
# de Futebol, na ordem de colocação. Depois mostre:
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética.
# Em que posição na tabela está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Brangantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'Os 5 primeiros colocados são: \n{times[:5]}')
print(f'Os ultimos 4 colocados são: \n{times[-4:]}')
print(f'Os times em ordem alfabética:\n{sorted(times)}')
print(f'Chapecoense está na posição: {times.index("Chapecoense") + 1}ª')
