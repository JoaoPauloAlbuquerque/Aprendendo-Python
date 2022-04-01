# Refaça o desafio 035 dos triângulos, acrescentando o recuso de mostrar
# que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais.
# ISÓSCELES: dois lados iguais.
# ESCALENO: todos os lados diferentes.

r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('É possível fazer um triângulo!')
    if r1 == r2 == r3:
        print('Triângulo: EQUILÁTERO')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Triângulo: ISÓRCELES')
    else:
        print('Triângulo: ESCALENO')
else:
    print('Não é possível fazer um triângulo!')
