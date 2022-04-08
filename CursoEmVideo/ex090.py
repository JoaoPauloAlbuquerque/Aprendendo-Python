# Faça um programa que leia nome e média de um aluno, guardando também
# a situação num dicionário. No final, mostre o conteúdo da estrutura.

aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
print('Situação é igual a ', end='')
if aluno['Média'] >= 7:
    print('Aprovado')
else:
    print('Reprovado')
