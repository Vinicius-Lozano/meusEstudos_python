print("\33[32m" + "~" * 150)
print('\33[34m' + f"{" Valores únicos em uma Lista ":=^150}")
print('\33[32m' + "~" * 150 + '\33[m')


num_list = []

while True:
    num = int(input('\33[34mAdicione um numero na lista:\33[33m '))
    
    if num not in num_list:
        num_list.append(num)
    else:
        print('\33[34mEsse numero ja esta na lista entao sera desconsiderado')
    
    stopper = input('\33[34mdeseja parar?\33[33m ').upper().strip()[0]
    if stopper in 'S':
        break

num_list.sort()

print('\33[32m' + "~" * 150 + '\33[m')
print(f'\33[34mA sua lista em ordem crescente:\33[33m {num_list}')
print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')