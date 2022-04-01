# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(0, 5):
    p = float(input('Digite seu peso: '))
    if maior == 0:
        maior = p
    elif p > maior:
        maior = p
    if menor == 0:
        menor = p
    elif p < menor:
        menor = p

print(f'Maior: {maior}')
print(f'Menor: {menor}')
