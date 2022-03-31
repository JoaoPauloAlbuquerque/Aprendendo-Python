# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de
# até 200km e R$0,45 para viagens mais longas.

n = float(input('Qual a distância da viagem (km): '))
if n <= 200:
    print(f'Sua viagem custará R${n * 0.5}')
else:
    print(f'Sua viagem custará R${n * 0.45}')
