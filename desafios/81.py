print("\33[32m" + "~" * 150)
print('\33[34m' + f"{' Extraindo dados de uma Lista ':=^150}")
print('\33[32m' + "~" * 150 + '\33[m')

num_list = []
stop = ''

print('\33[34mDigite os numeros ou coloque \33[31mp\33[34m para terminar')
num_find = int(input('Primeiro diga um Numero para encontrar: \33[33m '))

print('\33[32m' + "~" * 150 + '\33[m')

while True:
    
    entry = input('\33[32m=>\33[33m ')
    
    if entry == 'p':
        break
    
    num_list.append(int(entry))

# handlers
num_list_count = len(num_list)
num_list_dsort = sorted(num_list, reverse=True)


print('\33[32m' + "~" * 150 + '\33[m')

print(f'\33[34mVocê digitou esses numeros nessa ordem:\33[33m {' | '.join(str(n) for n in num_list)}')
print(f'\33[34mVocê digitou \33[33m{num_list_count}\33[34m Numeros')
print(f'\33[34mOs numeros digitados de forma Decresente: \33[33m{' | '.join(str(n) for n in num_list_dsort)}')

if num_find in num_list:
    num_find_pos = num_list.index(num_find) + 1
    print(f'\33[34mO número que você procura (\33[33m{num_find}\33[34m) esta na lista, e está na \33[33m{num_find_pos}ª\33[34m posiçao')
else:
    print('\33[34mO número que procura não esta na lista')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')