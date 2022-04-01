# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão
# 1 para binário
# 2 para octal
# 3 para hexadecimal

n = int(input('Digite um número inteiro: '))
print('Escolha 1 para binário')
print('Escolha 2 para octal')
print('Escolha 3 para hexadecimal')

e = int(input('Esolha: '))
if e == 1:
    print(f'A versão do número {n} em binário é = {format(n, "b")}')
elif e == 2:
    print(f'A versão do número {n} em octal é = {format(n, "o")}')
elif e == 3:
    print(f'A versão do número {n} em hexadecimal é = {format(n, "x")}')
else:
    print('Opção inválida...')
