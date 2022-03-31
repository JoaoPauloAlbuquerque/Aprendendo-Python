# Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

v = int(1250)
s = float(input('Digite o seu salário: '))
if s <= v:
    sa = s + (s * 0.15)
    print(f'O seu reajuste salarial será de R${sa}')
else:
    sa = s + (s * 0.1)
    print(f'O seu rajuste salarial será de R${sa}')
