# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante à função input() do python, entretanto fazendo a validação para aceitar
# apenas um valor numérico.

def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return n
        else:
            print(f'\033[31mERRO: Digite um número inteiro válido.\033[m')


p = leiaint('Digite um número: ')
print(f'Você acabou de digitar {p}')
