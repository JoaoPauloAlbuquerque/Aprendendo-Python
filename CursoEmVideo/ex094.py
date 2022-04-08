# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# Quantas pessoas foram cadastradas;
# A média de idade do grupo;
# Uma lista com todas as mulheres;
# Uma lista com todas as pessoas com idade acima da média;

pessoas = list()
pessoa = dict()
media = 0
cont = 0
mulheres = list()
pessoas_acima_media = list()
while True:
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['sexo'] = sexo
    pessoas.append(pessoa.copy())
    if sexo == 'F':
        mulheres.append(pessoa.copy())
    media += idade
    cont += 1
    saida = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if saida == 'N':
        break
media /= cont
print('-=' * 20)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for i in mulheres:
    print(f'[{i["nome"]}]', end=' ')
print()
print('- Lisca com as pessoas acima da média: ')
for i in pessoas:
    if i['idade'] > media:
        print()
        for k, v in i.items():
            print(f'{k} = {v}', end='; ')
        print()
