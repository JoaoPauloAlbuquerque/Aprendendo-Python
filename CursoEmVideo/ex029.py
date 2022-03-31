# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

v = int(input('Qual a velocidade do carro? '))
if v > 80:
    p = v - 80
    print(f'Você está acima da velicidade!')
    print(f'Sua multa será de R${p * 7},00')
else:
    print('Você está no limite de velocidade!')
