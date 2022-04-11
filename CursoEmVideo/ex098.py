# Faça um programa que tenha uma função chamda contador(), que receba três parâmetro:
# início, fim e passo, e realizar a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# De 1 até 10, de 1 em 1;
# De 10 até 0, de 2 em 2;
# Uma contagem personalizada.
from time import sleep


def contador(ini, fim, pas):
    pm = abs(pas)
    p = pas
    f = fim
    if ini > fim:
        f -= 1
        if pas > 0:
            p *= -1
        if pas == 0:
            p = -1
    else:
        f += 1
        if pas == 0:
            p = 1
    print('-=' * 30)
    print(f'Contagem de {ini} até {fim} de {pm} em {pm}')
    for i in range(ini, f, p):
        sleep(0.3)
        print(i, end=' ', flush=True)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua de personalizar a contagem!')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))
