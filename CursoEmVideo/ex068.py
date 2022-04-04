# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
count = 0
while True:
    computador = randint(0, 10)
    pessoa = int(input('Digite um valor de 0 a 10: '))
    escolha = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    total = computador + pessoa
    print(f'Total: {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
    if escolha == 'I':
        if total % 2 != 0:
            print('Você ganhou!')
        else:
            print('Você perdeu!')
            break
    count += 1
print(f'Você ganhou {count} vezes seguidas.')
