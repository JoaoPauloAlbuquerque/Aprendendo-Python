# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = list()
for i in range(0, 5):
    num = int(input(f'Digite o {i + 1}º valor: '))
    while num in lista:
        num = int(input(f'Valor já existe. Digite o {i + 1}º valor: '))
    if len(lista) == 0:
        lista.append(num)
        print(f'Inserido na posiçao 0')
    elif len(lista) == 1:
        if num > lista[0]:
            lista.append(num)
            print(f'Inserido na posiçao {len(lista) - 1}')
        else:
            lista.insert(0, num)
            print(f'Inserido na posiçao 0')
    else:
        for p, v in enumerate(lista):
            if num > v:
                if p + 1 != len(lista):
                    if num < lista[p + 1]:
                        lista.insert(p + 1, num)
                        print(f'Inserido na posiçao {p + 1}')
                else:
                    lista.append(num)
                    print(f'Inserido na posiçao {len(lista) - 1}')
            else:
                if num not in lista:
                    lista.insert(p, num)
                    print(f'Inserido na posição {p}')
print(lista)
