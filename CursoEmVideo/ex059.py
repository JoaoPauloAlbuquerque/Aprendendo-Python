# Cie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu prorgama deverá realizar a operação solicitada em cada caso.

while True:
    print('=-' * 20)
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print('''==OPÇÕES
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    o = int(input('Escolha: '))
    if o == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif o == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif o == 3:
        if n1 > n2:
            print(f'O número maior é {n1}')
        elif n2 > n1:
            print(f'O número maior é {n2}')
        else:
            print(f'Os dois números são iguais')
    elif o == 4:
        print('Digite novos valores:')
    elif o == 5:
        break
    else:
        print('Opção inválida...')
print('Programa finalizado!')
