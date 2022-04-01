i = int(input('Digite um número: '))
if i > 1:
    if i < 10:
        print(f'{i} é maior que 1 e menor que 10')
    else:
        print(f'{i} é maior que 1 e também é maior que 10')
else:
    print(f'{i} é menor que 1')
