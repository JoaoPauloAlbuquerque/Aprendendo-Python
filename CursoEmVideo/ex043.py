# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# o seu IMC e mostre o seu status, conforme a tabela abaixo:
# Abaixo de 18.5: abaixo do peso.
# Entre 18.5 e 25: peso ideal.
# 25 até 30: sobrepeso.
# 30 até 40: obesidade.
# Acima de 40: obesidade mórbida.

p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = float(p / (a ** 2))
if imc < 18.5:
    print(f'imc igual a {imc:.2f}: abaixo do peso')
elif imc <= 25:
    print(f'imc igual a {imc:.2f}: peso ideal')
elif imc <= 30:
    print(f'imc igual a {imc:.2f}: sobrepeso')
elif imc <= 40:
    print(f'imc igual a {imc:.2f}: obesidade')
else:
    print(f'imc igual a {imc:.2f}: obesidade mórbida')
