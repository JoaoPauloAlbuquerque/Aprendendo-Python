# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
# em uma lista composta. No final, mostre um boletim contendo a média de cada um e permit
# que o usuário possa mostrar as notas de cada aluno individualmente.

lista = list()
while True:
    aluno = list()
    notas = list()
    aluno.append(str(input('Nome do aluno: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    lista.append(aluno[:])
    aluno.clear()
    notas.clear()
    f = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if f in 'Nn':
        break
media = 0
no = 'No.'
nome = 'NOME'
med = 'MÉDIA'
print('-=' * 30)
print(f'{no:<5}{nome:<15}{med:>3}')
print('_' * 30)
for pAlunos, aluno in enumerate(lista):
    print(f'{pAlunos:<5}{aluno[0]:<15}', end=' ')
    for pDados, dados in enumerate(aluno[1]):
        media += dados
    media /= 2
    print(f'{media:>3.1f}', end=' ')
    print()
    media = 0
print('_' * 30)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    if n < len(lista):
        print(f'As notas de {lista[n][0]} são {lista[n][1]}')
    print('_' * 30)
