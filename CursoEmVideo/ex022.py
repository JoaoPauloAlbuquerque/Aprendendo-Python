# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras tem o nome completo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(len(nome.split()[0]))
