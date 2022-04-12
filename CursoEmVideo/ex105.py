# Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguntes informações:
# Quantidade de notas;
# - A maior nota;
# - A menor nota;
# - A média da turma;
# - S situação (opcional)
# Adicione também sa docstrings da função

def notas(*n, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turna.
    """
    total = len(n)
    maior = max(n)
    menor = min(n)
    media = sum(n) / total
    dic = {
            'total': total,
            'maior': maior,
            'menor': menor,
            'média': f'{media:.1f}'
        }
    if sit:
        dic['situação'] = 'APROVADO' if media >= 7 else 'REPROVADO'
    return dic


resp = notas(5.5, 9.5, 5, 6.4, sit=True)
print(resp)
