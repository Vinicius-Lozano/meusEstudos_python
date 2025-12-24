print("\33[1;32m" + "~" * 150)
print('\33[34m' + f"{' Dividindo valores em várias listas ':=^150}")
print('\33[1;32m' + "~" * 150 + '\33[m')

#lists
num_list = []
num_even_list = []
num_odd_list = []

#get numbers
print('\33[34mDigite um numero ou (\33[33ms\33[34m) para Sair:')
while True:
    try:
        num_input = int(input("\33[33m=>\33[1;31m "))
        num_list.append(num_input)     
    except:
        break

#sort in lists

for num in num_list:
    if num % 2 == 0:
        num_even_list.append(num)
    else:
        num_odd_list.append(num)

num_list.sort()
num_even_list.sort()
num_odd_list.sort()
   
print('\33[32m' + "~" * 150 + '\33[m')

print(f'\33[34mNo Total você digitou os numeros => \33[1;33m {' | '.join(str(n) for n in num_list)}')
print(f'\33[0;34mDos numeros digitados esses são os pares => \33[1;33m{' | '.join(str(n) for n in num_even_list)}')
print(f'\33[0;34mDos numeros digitados esses são os impares => \33[1;33m{' | '.join(str(n) for n in num_odd_list)}')

print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')