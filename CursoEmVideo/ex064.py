# Crie um programa que leia vários números inteiros do teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram figitados e qual foi a soma entre eles
# (desconsiderando o flag).
quanti = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    quanti += 1
print(f'Foram digitados {quanti} números')
print(f'A soma deles deu um total de {soma}')
