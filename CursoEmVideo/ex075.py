# Desenvolva um programa que leia quatro valores pelo teclado e garde-os em uma tupla.
# No final, mostre:
# Quantas vezes apareceu o valor 9;
# Em que posição foi digitado o primeiro valor 3;
# Quais foram os números pares;

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
lista = (n1, n2, n3, n4)
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if lista.count(3) > 0:
    print(f'O primeiro valor 3 aparece na {lista.index(3) + 1}ª posição')
else:
    print('O valor 3 aparece nenhuma vez')
print('Os números pares foram:', end=' ')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
