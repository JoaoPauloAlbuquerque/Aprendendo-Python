# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
print('Digite 0 para o ano atual.')
a = int(input('Digite um ano qualquer: '))
if a == 0:
    a = date.today().year # Pega o ano atual do computador
if ((a % 4) == 0 and (a % 100) != 0) or (a % 400) == 0:
    print(f'O ano {a} é bissexto!')
else:
    print(f'O ano {a} não é bissexto!')
