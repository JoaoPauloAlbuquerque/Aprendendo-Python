# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for c in range(0, 7):
    a = int(input('Digite o seu ano de nascimento: '))
    idade = date.today().year - a
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(f'Maior: {maior}')
print(f'Menor: {menor}')
