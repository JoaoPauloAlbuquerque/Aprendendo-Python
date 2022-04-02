# Cria um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valore lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = 0
quanti = 0
maior = 0
menor = 0
while True:
    n = int(input('Digite um número inteiro: '))
    soma += n
    quanti += 1
    if quanti == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    condicao = str(input('Você deseja continuar digitando? [S/N]')).strip().upper()[0]
    if condicao == 'N':
        break
print('=-' * 30)
media = soma / quanti
print(f'Foram digitados {quanti} números e a média é {media:.2f}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
