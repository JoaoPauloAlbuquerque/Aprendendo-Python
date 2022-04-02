# Melhore o desafio 061, perguntanto para o usuário se ele quer
# mostrar mais alguns termos. O programa encerra quando ele disse que quer
# mostrar 0 termos.


p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
# Fórmula para calcular o enézimo termo de uma PA
# posicao = primeiro + (enézimo - 1) * razão
t = 10
count = 0
while t != 0:
    decimo = p + (t - 1) * r
    while p <= decimo:
        print(p, end=' ')
        p += r
        count += 1
    t = int(input('\nDeseja mostrar mais quantos termos da PA? '))
print(f'O prigrama finalizou com {count} itens mostrados.')
