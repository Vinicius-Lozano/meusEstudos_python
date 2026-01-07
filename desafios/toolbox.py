res = 60
    
cores = {
    'azul': '\33[1;34m',
    'verde': '\33[1;32m',
    'amarelo': '\33[1;33m'}
    
def cabecalho(text):
    print("\33[1;32m" + "~" * res)
    print('\33[34m' + f"{text:=^{res}}")
    print('\33[1;32m' + "~" * res + '\33[m')

def paragrafo(text, cor='verde'):
    print(cores[cor] + f"{text:~^{res}}" + '\33[m')
    
def linha(char='~', cor='verde'):
    print(cores[cor] + char * res + '\33[m')
    
def fimLinha(fim='FIM'):
    fim = f' {fim} '
    print(f'\33[1;33m{fim:x^{res}}\33[0;m')