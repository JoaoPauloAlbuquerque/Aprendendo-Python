# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeir e o último nome separadamente.

n = str(input('Digite seu nome completo: '))
lista = n.split()
print(f'Primeiro nome: {lista[0]}')
print(f'Último nome: {lista[len(lista) - 1]}')
