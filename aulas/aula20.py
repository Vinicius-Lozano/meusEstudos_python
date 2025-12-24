def soma(a, b):
    s = a + b
    print(f'\33[34mA soma de \33[33m{a} \33[34m+ \33[33m{b} \33[34mé igual a \33[33m{s}\33[m')

def contador(*num):
    print(num)

def dobralista(lst):
    for n in range(len(lst)):
        lst[n] *= 2
    print(lst)


soma(1,2)
soma(b=2, a=1)

contador(1, 2, 3, 4)
contador(1, 2)

lista = [1,2]
dobralista(lista)

