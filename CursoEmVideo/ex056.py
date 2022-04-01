# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do home mais velho.
# Quantas mulheres tem menos de 20 anos.
m = 0
mIdade = 0
h = ''
q = 0
for c in range(0, 4):
    print('-' * 20)
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
    m += idade

    if mIdade == 0 and sexo == 'M':
        mIdade = idade
        h = nome
    elif idade > mIdade and sexo == 'M':
        mIdade = idade
        h = nome

    if idade < 20 and sexo == 'F':
        q += 1

print('=-' * 20)
m = m / 4
print(f'A média de idade é: {m:.2f}')
print(f'Maior idade masculina é: {h}')
print(f'Mulheres menores de 20 anos: {q}')
