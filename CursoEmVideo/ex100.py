# Faça um programa que tenha uma lista chamda números e duas funções
# chamdas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro de umalista e a segunda irá mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint as rd
from time import sleep


def sorteia():
    lista = [
        rd(0, 10),
        rd(0, 10),
        rd(0, 10),
        rd(0, 10),
        rd(0, 10)
    ]
    print('Sortando 5 valores da lista: ', end='')
    for i in lista:
        sleep(0.5)
        print(i, end=' ')
    print('PRONTO!')
    return lista


def somapar(lista):
    print(f'Somando os valores pares de {lista}, temos ', end='')
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(s)


somapar(sorteia())
