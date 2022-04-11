# Faça um programa que tenha uma função chamda maior(), que receba vários parâmetros
# com valores interios. Seu programa tem que analizar todos os valores e dizer qual dele é o maior.
from time import sleep


def maior(*n):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for i in n:
        sleep(0.5)
        print(i, end=' ')
    print(f'Foram informados {len(n)} ao todo.')
    if len(n) == 0:
        print('O maior valor informado foi 0.')
    else:
        print(f'O maior valor informado foi {max(n)}.')


maior(1, 2, 3, 67, 3, 9)
maior(9, 3, 4, 1, 5)
maior(44, 22, 99)
maior(9, 2)
maior(76)
maior()
