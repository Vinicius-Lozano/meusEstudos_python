import toolbox

toolbox.cabecalho(' Um print especial ')

def escreva (text):
    tamanho = len(text) + 4
    linha = '~' * tamanho
    
    print(f'\33[32m{linha:^60}')
    print(f"{text:^{tamanho}}".center(60))
    print(f'\33[32m{linha:^60}')
    
texto = str(input('\33[34mQual texto deseja escrever?\33[33m '))
print('\33[m', end='')
escreva(texto)

toolbox.fimLinha()