# Crie um programa que tenha um tupla única com nomes de produtos
# e os seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (
    'Coca-Cola', 7.5,
    'Feijão', 6,
    'Arroz', 4.5,
    'Macarrão', 3.75,
    'Mortadela', 35,
    'Carne', 45.5,
    'Queijo', 15.3
)

for p in range(0, len(produtos), 2):
    print(f'{produtos[p]:.<30}:R$ {produtos[p + 1]:>7.2f}')
