def aumentar(num, tax):
    res = num + (num * tax/100)
    return res

def diminuir(num, tax):
    res = num - (num * tax/100)
    return res

def dobro(num):
    res = num * 2
    return res

def metade(num):
    res = num / 2
    return res

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num}'.replace('.', ',')