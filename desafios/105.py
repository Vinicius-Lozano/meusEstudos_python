import toolbox

toolbox.cabecalho(' Analisando e gerando Dicionários ')

def notas(*num, sit=False):
    '''
    Docstring for notas
    
    :param num: todas as notas
    :param sit: Desliga ou liga a situação
    '''
    notas = sorted(num)
    media = sum(notas) / len(notas)
    aluno = {'Total': len(notas), 'Maior': max(notas), 'Menor': min(notas), 'Media': f'{media:.2f}'}
    
    if sit:
        if media >= 7:
            aluno['situação'] = 'BOA'
        elif media >= 5:
            aluno['situação'] = 'RAZOAVEL'
        else:
            aluno['situação'] = 'RUIM'
            
    return aluno

aluno_sit = notas(7, 6, 3, 2, sit=True)
print(f'\33[34m{aluno_sit}')
toolbox.fimLinha()