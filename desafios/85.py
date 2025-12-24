print("\33[1;32m" + "~" * 150)
print('\33[34m' + f"{' Listas com pares e impares ':=^150}")
print('\33[1;32m' + "~" * 150 + '\33[m')

num_even = []
num_odd = []
print('\33[34mDigite os numeros: ')
for q in range(0, 7):
    
    num = int(input('\33[0;34m=>\33[1;33m '))
    
    if num % 2 == 0:
        num_even.append(num)
    else:
        num_odd.append(num)

num_even.sort()
num_odd.sort()

numbrs = [num_odd[:], num_even[:]]

print('\33[1;32m' + "~" * 150 + '\33[m')
print(f'\33[34mOs numeros impares são \33[1;33m{' | '.join(str(n) for n in numbrs[0])} ')
print(f'\33[0;34mOs numeros pares são \33[1;33m{' | '.join(str(n) for n in numbrs[1])} ')
print('\33[33m' + '\33[1;31m FIM \33[0;33m'.center(164, 'x'), '\33[m')