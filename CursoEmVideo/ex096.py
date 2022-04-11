# Faça um programa que tenha uma função chamda área(), que recebe as dimensões
# de um terreno retangulo (largura e comprimento) e mostre a área do terreno.

def area(larg, alt):
    a = larg * alt
    print(f'A área de um terreno {larg}x{alt} é de {a}m².')


largura = float(input('LARGURA (m): '))
altura = float(input('ALTURA (m): '))
area(largura, altura)
