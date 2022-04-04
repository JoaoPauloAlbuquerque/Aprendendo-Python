# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos;
# Quantos homens foram cadastrados;
# Quantas mulheres tem menos de 20 anos;

pessoasmaioridade = 0
homenscadastrados = 0
mulhermaisvinteanos = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        pessoasmaioridade += 1
    if sexo == 'M':
        homenscadastrados += 1
    if sexo == 'F' and idade > 20:
        mulhermaisvinteanos += 1
    repi = ' '
    while repi not in 'SN':
        repi = str(input('Deseja cadastrar novamente? [S/N] ')).strip().upper()[0]
    if repi == 'N':
        break
print(f'Pessoas maior de 18 anos: {pessoasmaioridade}')
print(f'Homens cadastrados: {homenscadastrados}')
print(f'Mulheres com mais de 20 anos: {mulhermaisvinteanos}')
