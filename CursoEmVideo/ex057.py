# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente at[e ter um valor correto.

p = True
while p:
    s = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if s in 'MF':
        p = False
