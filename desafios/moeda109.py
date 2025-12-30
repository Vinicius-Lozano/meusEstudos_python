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
