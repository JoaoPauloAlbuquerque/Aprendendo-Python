# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    saida = str(input('Deseja sair do programa? [S/N] ')).strip().upper()[0]
    if saida == 'S':
        break
par = list()
impar = list()
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Todos os números: {lista}')
print(f'Números impares: {impar}')
print(f'Números pares: {par}')
