# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
'''
 Quando você tem um número (ex: 1234)
 e faz uma divisão inteira dele por 10,
 o que resta é 123, e fazendo o resto da 
 divisão de 123 por 10, o que resta é 12,3
 mas como o % pega apenas o resto, o que é pego 
 é apenas o ,3 ou seja, o 3.
'''
d = n // 10 % 10
'''
 Quando você faz a divisão inteira de 1234
 por 100, o que resta é 12, em seguida fazendo 
 o resto da divisão por 10, o que resta é 1,2
 porém, como o % pega apenas o resto, o que é 
 restornado é ,2 ou seja, 2.
'''
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
