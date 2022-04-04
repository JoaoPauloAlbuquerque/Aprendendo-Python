# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Aprender', 'Programar', "Estudar", 'Python', 'Escada', 'Sucesso',
            'Casa', 'Computador', 'Linguagem', 'Escola', 'Curso', 'Aulas')
vogais = 'aeiouAEIOU'
for p in palavras:
    print(f'\nPara a palavra {p.upper()} temos as vogais: ', end=' ')
    for v in p:
        if v in vogais:
            print(v.lower(), end=' ')
