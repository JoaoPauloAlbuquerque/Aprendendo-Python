# Crie um prorgama que leia o nome de uma cidade e diga
# se ela começa ou não com o nome "SANTO"

n = str(input('Digite um nome de cidade: ')).strip()
p = n.split()[0]
print(f'Começa com "SANTO": {"SANTO" in p.upper()}')
