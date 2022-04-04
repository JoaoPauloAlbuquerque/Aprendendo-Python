# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
while True:
    v = int(input('Digite um valor para saque: '))
    cinquenta = v // 50
    falta = v - (cinquenta * 50)
    vinte = falta // 20
    falta -= vinte * 20
    dez = falta // 10
    falta -= dez * 10
    um = falta // 1
    falta -= um * 1
    if cinquenta != 0:
        print(f'{cinquenta} notas de R$50')
    if vinte != 0:
        print(f'{vinte} notas de R$20')
    if dez != 0:
        print(f'{dez} notas de R$10')
    if um != 0:
        print(f'{um} notas de R$1')
    saida = str(input('Deseja fazer outro saque: [S/N] ')).upper().strip()[0]
    if saida == 'N':
        break
