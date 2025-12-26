import toolbox
from random import randint

toolbox.cabecalho(' Funções para sortear e somar ')

def sorteia(num):
    return [randint(1, 20) for _ in range(num)]

def somaPar(numbrs):
    num_par = []
    for num in numbrs:
        if num % 2 == 0:
            num_par.append(num)
    print(f'\33[34mA soma dos numeros pares da sua lista é: \33[33m{num_par} \33[34mé \33[33m{sum(num_par)}\33[m')

lista_num = sorteia(5)
print(f'\33[34mEssa lista foi sorteada: \33[33m{lista_num}')
somaPar(lista_num)

toolbox.fimLinha()