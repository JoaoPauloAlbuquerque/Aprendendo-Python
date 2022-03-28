# Faça um programa que leia a largura e a altura de uma
# parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2m².

largura = float(input('Digite a largura da parede (metros): '))
altura = float(input('Digite a altura da parede (metros): '))
area = largura * altura
print(f'Precisa de {area / 2}L de tinta para pintar uma parede de {area}m²')
