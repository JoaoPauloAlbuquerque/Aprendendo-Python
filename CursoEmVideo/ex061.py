# Refaça o desafio 051, lendo o primeiro termo de uma PA, mostrando os 10
# primeiros termos da progressão usando a estrutura while.

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
# Fórmula para calcular o enézimo termo de uma PA
# posicao = primeiro + (enézimo - 1) * razão
decimo = p + (10 - 1) * r
while p <= decimo:
    print(p)
    p += r
