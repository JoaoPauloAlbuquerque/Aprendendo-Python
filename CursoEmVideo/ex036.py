# Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado.

valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = float(input('Em quantos anos quer pagar: '))

quanti_meses = int(anos * 12)
parcela_mensal = valor_casa / quanti_meses
percent_salario = salario * 0.3

if parcela_mensal <= percent_salario:
    print('Compra realizada')
    print(f'Valor percela: R${parcela_mensal:.2f}')
    print(f'Quanti. parcela: {quanti_meses}')
else:
    print('Não foi possível fazer a venda...')
    print(f'Pode pagar: R${percent_salario:.2f}')
    print(f'Valor percela: R${parcela_mensal:.2f}')
    print(f'Quanti. parcela: {quanti_meses}')
