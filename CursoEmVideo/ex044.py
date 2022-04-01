# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pragamento:
# Á vista dinheiro/cheque: 10% de desconto.
# Á vista no cartão: 5% de desconto.
# Em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros.

preco = float(input('Qual o preço do produto: '))
print('=-' * 20)
print('Formas de pagamento')
print('=-' * 20)
print('1 - avista dinheiro/cheque')
print('2 - avista cartão')
print('3 - em 2x no cartão')
print('4 - em 3x ou mais no cartão')
pagamento = int(input('Escolha: '))
if pagamento == 1:
    print(f'Valor total: R${preco - (preco * 0.1):.2f}')
elif pagamento == 2:
    print(f'Valor total: R${preco - (preco * 0.05):.2f}')
elif pagamento == 3:
    print(f'Valor total: R${preco:.2f}')
elif pagamento == 4:
    print(f'Valor total: R${preco + (preco * 0.2)}')
else:
    print('Opção inválida...')
