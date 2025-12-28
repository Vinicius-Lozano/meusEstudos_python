import toolbox

toolbox.cabecalho(' Validando entrada de dados ')

def leiaInt():
    while True:
        try:
            inp = int(input('\33[34mDigite um numero:\33[33m '))
        except:
            print('\33[31mVoçe não digitou um numero!')
            continue
        return inp

num = leiaInt()
print(f'\33[34mVoçe digitou o numero \33[33m{num}')

toolbox.fimLinha()