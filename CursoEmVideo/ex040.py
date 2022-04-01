# Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, conforme a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

cor = {
    'none': '\033[m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'vermelho': '\033[31m'
}

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua nota: '))
m = float((n1 + n2) / 2)
if m < 5.0:
    print(f'Sua média foi de {m:.1f}: {cor["vermelho"]}REPROVADO')
elif 5.0 <= m < 7:
    print(f'Sua média foi de {m:.1f}: {cor["amarelo"]}RECUPERAÇÃO')
else:
    print(f'Sua média foi de {m:.1f}: {cor["verde"]}APROVADO')
