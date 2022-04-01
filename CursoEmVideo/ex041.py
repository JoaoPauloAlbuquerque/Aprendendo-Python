# A confederação Nacional de Natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre a sua categoria, conforme a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date
a = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - a
if idade <= 9:
    print(f'{idade} anos: MIRIN')
elif idade <= 14:
    print(f'{idade} anos: INFANTIL')
elif idade <= 19:
    print(f'{idade} anos: JUNIOR')
elif idade <= 20:
    print(f'{idade} anos: SÊNIOR')
else:
    print(f'{idade} anos: MASTER')
