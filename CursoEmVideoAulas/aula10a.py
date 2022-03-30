n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média foi {m:.2f}')
if m >= 6:
    print('Parabéns, você foi aprovado!')
else:
    print('Estude mais da próxima vez!')

# Outra forma de fazer um if
print('Parabéns, você foi aprovado!' if m >= 6 else 'Estude mais da próxima vez!')
