# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
# (com idade) num dicionário, se por acaso o CTPS for diferente de zero, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente, além da
# idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
p = dict()
nome = str(input('Digite seu nome: '))
ano = int(input('Em que ano você nasceu: '))
ctps = int(input('Carteira de trabalho (0 se não ter): '))

idade = date.today().year - ano
p['nome'] = nome
p['idade'] = idade
p['ctps'] = ctps
if ctps != 0:
    contratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    p['contratacao'] = contratacao
    p['salário'] = salario
    aposentadoria = (contratacao + 35) - ano
    p['aposentadoria'] = aposentadoria
print('-=' * 20)
for k, v in p.items():
    print(f'{k} tem o valor {v}')
