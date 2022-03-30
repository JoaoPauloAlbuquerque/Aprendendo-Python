s = '   João Paulo de Albuquerque Santos    '
print(s)
# Imprimindo apenas uma letra da string.
print(s[5])
# Imprimindo de uma posição até outra.
print(s[5:10])
# Imprimindo da primeira posição até uma determinada posição.
print(s[:10])
# Imprimindo de uma posição até a última.
print(s[11:])
# Imprimindo posições intercaladas a cada dois.
print(s[::2])
# Tamanho de uma string.
print(len(s))
# Contar quantas vezes um caracter aparece na string.
# Este método diferencia letras maiúsculas, minúsculas e com acentos.
print(s.count('a'))
# Deixar todas as letras maiúsculas.
print(s.upper())
# Deixar todas as letras minúsculas.
print(s.lower())
# Remove os espaços do começo e fim da string.
print(s.strip())
# Remove os espaços apenas do começo da string.
print(s.rstrip())
# Remove os espaços apenas do fim da string.
print(s.lstrip())
# Trocar palavras, onde o primeiro argumento é o que
# você quer trocar, e o segundo é pelo que você quer trocar.
print(s.replace('Santos', 'Silva'))
print(s.strip().replace(' ', '-'))  # Adicionando um '-' onde tiver um espaço.
# Verificando se existe uma palavra dentro de uma frase.
print('João' in s)
# Mostra a posição onde começa a palavra dentro da string.
print(s.find('João'))
# Divide a frase em cada palavra, formando assim, uma lista.
print(s.split())
