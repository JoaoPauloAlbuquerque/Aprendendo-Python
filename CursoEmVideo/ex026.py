# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

n = str(input("Digite seu nome: ")).strip().upper()
print(f'Apreceu a letra "A" {n.count("A")} vezes')
print(f'Primeira vez que aparece: {n.find("A") + 1}ª posição')
print(f'Última vez que aparece: {n.rfind("A") + 1}ª posição')
