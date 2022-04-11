def lin(text):
    print('-' * 30)
    print(f'{text:^30}')
    print('-' * 30)


def divi(a, b):
    return a / b


# Receber vários parâmetros na função
# o *num se transforma em uma túpla
def contador(*num):
    print(f'Foi passado {len(num)} parâmetros')


lin('Curso em Vídeo')
s = divi(5, 1)
s1 = divi(b=2, a=9)
print(s)
print(s1)

contador(1, 2, 3)
contador(2, 3, 4, 5, 6, 7)
