# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
# pessoa tem voto negado, opciona ou obrigatório ns eleições.

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade <= 60:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


print(voto(int(input('Em que ano você nasceu? '))))
