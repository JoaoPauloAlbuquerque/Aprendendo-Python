# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# ou fechados na ordem correta.

ex = str(input('Digite sua expressão: ')).strip()
lista = list()
for i in ex:
    lista.append(i)
count1 = lista.count('(')
count2 = lista.count(')')
if count1 != count2:
    print('Expressão está incorreta.')
else:
    print('Expressão está correta.')
