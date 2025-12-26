import toolbox
from time import sleep
toolbox.cabecalho(' Função que descobre o maior ')

def maior(* num):
    print('\33[34mAnalisando Numeros...\33[33m')
    
    if len(num) != 0:
        for n in num:
            print(f'{n}', end= ' ', flush= True)
            sleep(0.5)
    else:
        print('\33[31mNão foi informado nenhum valor\33[m')
        return 
    
    numbrs = sorted(list(num))
    
    print(f'\33[34mfoi informado \33[33m{len(numbrs)} \33[34mvalores e o maior deles foi \33[33m{max(numbrs)}\33[m')
    
maior(9, 8, 7)
toolbox.linha()

maior(1, 3, 5, 7, 8, 10, 11)
toolbox.linha()

maior(1, 3)
toolbox.linha()

maior()
toolbox.fimLinha()
