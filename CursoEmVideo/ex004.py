# Faça um programa que leia algo pelo teclado e mostre na
# tela o tipo primitivo e todas as informações possíveis sobre ele.

v = input('Digite algo: ')
print(f'\nDigitado.................: {v}')
print(f'Tipo.....................: {type(v)}')
print(f'Apenas espaço............: {v.isspace()}')
print(f'Apenas Letra.............: {v.isalpha()}')
print(f'Apenas número............: {v.isnumeric()}')
# se contiver espaços, retornará falso
print(f'Apenas número e/ou letra.: {v.isalnum()}')
print(f'Digit....................: {v.isdigit()}')
print(f'Apenas minúsculo.........: {v.islower()}')
print(f'Apenas maiúsculo.........: {v.isupper()}')
# este comando verifica se o que foi digitado está em maiúscula e minúscula simultâneamente
print(f'Está capitalizado........: {v.istitle()}')
print(f'Printável................: {v.isprintable()}')
