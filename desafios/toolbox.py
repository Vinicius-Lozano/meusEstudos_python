res = 60

def cabecalho(text):
    print("\33[1;32m" + "~" * res)
    print('\33[34m' + f"{text:=^{res}}")
    print('\33[1;32m' + "~" * res + '\33[m')

def paragrafo(text):
    print('\33[34m' + f"{text:~^{res}}" + '\33[m')
    
def linha():
    print('\33[1;32m' + "~" * res + '\33[m')
    
def fimLinha(fim='FIM'):
    fim = f' {fim} '
    print(f'\33[1;33m{fim:x^{res}}\33[0;m')