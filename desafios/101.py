import toolbox
from datetime import datetime
toolbox.cabecalho(' Funções para votação ')

def voto(year):
    idade =  datetime.now().year - year
    if idade >= 65:
        res = 'VOTO OPCIONAL'
    elif idade >= 18:
        res = 'VOTO OBRIGATORIO'
    else:
        res = 'NEGADO'
    return {'idade': idade, 'resultado': res}

ano = int(input('\33[34mQual o ano de nascimento? \33[33m'))
resultado = voto(ano)
print(f'\33[34mCom \33[33m{resultado['idade']} \33[34mAnos: \33[31m{resultado['resultado']}')
toolbox.fimLinha()