import toolbox

toolbox.cabecalho(' Função para fatorial ')

def fatorial(num, show=False):
    '''
    Docstring for fatorial
    
    :param num: Description
    :param show: Description
    '''
    f = 1
    showcalc = []
    for c in range(num, 0, -1):
        f *= c
        if show is True:
            showcalc.append(c)
    if show:
        return f"{' x '.join(map(str, showcalc))} = {f}"
    else:
        return f
    
print(fatorial(5))
toolbox.linha()

print(fatorial(5, show=True))
toolbox.fimLinha()