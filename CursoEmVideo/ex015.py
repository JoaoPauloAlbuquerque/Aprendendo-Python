# Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por km rodado.

km = float(input('Quantos km rodados: '))
dias = int(input('Quantos dias: '))
print(f'Custo total de R${(0.15 * km) + (60 * dias)}')
