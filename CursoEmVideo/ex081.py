# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# Quantos números foram digitados;
# A lista de valores, ordenada de forma decrescente;
# Se o valor 5 foi digitado e está ou não na lista;

lista = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    saida = str(input('Deseja sair do programa? [S/N] ')).strip().upper()[0]
    if saida == 'S':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(lista)
print('O 5 está na lista' if 5 in lista else 'O 5 não está na lista')
