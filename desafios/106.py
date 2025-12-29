import toolbox

toolbox.cabecalho(' Interactive helping system in Python ')

def ajuda():
    while True:
        comando = input('\033[34mDigite a função ou biblioteca (ou "fim" para sair): \033[33m').strip().lower()
        
        if comando in ('fim', 'q'):
            print('\033[31mATÉ LOGO!\033[m')
            break
        
        print('\033[m') 
        help(comando)

ajuda()