# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
from builtins import reversed

lista = list()
while True:
    num = int(input('Digite um valor: '))
    if num < 0:
        break
    if num not in lista:
        lista.append(num)
        print(lista)
    else:
        print('Ítem já existe na lista.')
lista.sort()
print(lista)
