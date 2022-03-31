# desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('É possível fazer um triângulo!')
else:
    print('Não é possível fazer um triângulo!')
