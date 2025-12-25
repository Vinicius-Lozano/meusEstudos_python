import toolbox
from time import sleep
toolbox.cabecalho(' Função de Contador ')

def contador(inc, fim, pas):
    
    pas = abs(pas) if pas != 0 else 1
    sobra = abs(fim - inc) % pas
    
    print(f'\33[34mContagem de \33[33m{inc} \33[34maté \33[33m{fim} \33[34mcom passo \33[33m{pas}')

    fimb = fim + 1 if inc < fim else fim -1
    pasb = pas if inc < fim else -pas
    
    for n in range(inc, fimb, pasb):
        print(n, end= ' ', flush= True)
        sleep(0.2)

    print('\33[31mFim!') if sobra == 0  else print(f'\33[31m - Sobrou {sobra} Fim!')
    
contador(1, 10, 1)
toolbox.linha()

contador(10, 0, 2)
toolbox.linha()

print('\33[34mEscolha as posiçoes: ')
inicio = int(input('\33[34mInício =>\33[33m '))
fim = int(input('\33[34mFim =>\33[33m '))
passo = int(input('\33[34mPasso =>\33[33m '))

toolbox.paragrafo(' Contagem ')

contador(inicio, fim, passo)
toolbox.fimLinha()
