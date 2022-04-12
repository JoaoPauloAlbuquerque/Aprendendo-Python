# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamdo show, que será
# um valor lógico (opcional) indicando se será mostrado ou não na tela o processo
# de cáculo do fatorial.

def fatorial(n, show=False):
    """
    -> Calcular o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    r = ''
    print('-' * 30)
    for i in range(n, 0, -1):
        f *= i
        if show:
            if i == 1:
                r += f' {i} = {f}'
            else:
                r += f' {i} x'
        else:
            r = f
    return r


print(fatorial(5))
