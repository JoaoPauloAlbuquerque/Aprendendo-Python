# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. O programa
# será interrompido quando o número solicitado foir negativo.

while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('-' * 30)
