def cabecalho(text):
    print("\33[1;32m" + "~" * 145)
    print('\33[34m' + f"{text:=^145}")
    print('\33[1;32m' + "~" * 145 + '\33[m')

def linha():
    print('\33[1;32m' + "~" * 145 + '\33[m')
    
def fimLinha():
    print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(159, 'x'), '\33[0;m')