import toolbox

toolbox.cabecalho(' Funçoes aprofundadas ')

def leiaInt(inpint=0):
    while True:
        try:
            inpint = int(input('\33[34mDigite um numero inteiro:\33[33m '))
        except (ValueError, TypeError):
            print('\33[31mVoçe não digitou um numero!')
            continue
        return inpint

def leiafloat(inpfloat=0):
    while True:
        try:
            inpfloat = float(input('\33[34mDigite um numero real:\33[33m '))
        except (ValueError, TypeError):
            print('\33[31mVoçe não digitou um numero!')
            continue
        return inpfloat

numeroInt = leiaInt()
numeroReal = leiafloat()
print(f'\33[34mO numero inteiro digitado foi : \33[33m{numeroInt} \33[34me o numero real foi \33[33m{numeroReal}')