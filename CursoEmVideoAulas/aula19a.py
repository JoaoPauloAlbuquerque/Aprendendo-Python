dicionario = dict()
pessoas = {'nome': 'João Paulo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
print('Chaves: ')
for k in pessoas.keys():
    print(k)
print('Valores: ')
for v in pessoas.values():
    print(v)
print('Chave = valor')
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = list()
estado1 = {'uf': 'Alagoas', 'sigla': 'AL'}
estado2 = {'uf': 'Pernambuco', 'sigla': 'PE'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['uf'])

estado = dict()
brasil.clear()
for c in range(0, 2):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
print(brasil)
