# Faça um programa que leia o ano de nascimento de um jovem e informe,
# conforme a sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alista.
# Se já passou do tempo do alistamento.
# O seu programa derá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

a = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - a
if idade < 18:
    print(f'Está faltando {18 - idade} anos para se alistar ao serviço militar.')
elif idade == 18:
    print(f'Está na hora de se alistar.')
else:
    print(f'Já passou {idade - 18} anos do seu alistamento militar.')
