# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.

lista = list()
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi {max(lista)} na {lista.index(max(lista)) + 1}ª posição')
print(f'O menor valor digitado foi {min(lista)} na {lista.index(min(lista)) + 1}ª posição')
