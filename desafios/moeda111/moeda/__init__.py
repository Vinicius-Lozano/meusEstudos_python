def aumentar(num, tax, format = False):
    res = num + (num * tax/100)
    return res if not format else moeda(res)

def diminuir(num, tax, format=False):
    res = num - (num * tax/100)
    return res if not format else moeda(res)

def dobro(num, format=False):
    res = num * 2
    return res if not format else moeda(res)

def metade(num, format=False):
    res = num / 2
    return res if not format else moeda(res)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num}'.replace('.', ',')

def resumo(num, dim=20, aum=25):
    print('~' * 60)
    print(f'{'Resumo':^60}')
    print('~' * 60)
    print('Dobro:'.ljust(30), dobro(num, format=True))
    print('Metade:'.ljust(30), metade(num, format=True))
    print(f'{aum}% de aumento:'.ljust(30), aumentar(num, aum,format=True))
    print(f'{dim}% de redução:'.ljust(30), aumentar(num, dim,format=True))
    print('~' * 60)