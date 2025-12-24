print("\33[1;32m" + "~" * 150)
print('\33[34m' + f"{' mais sobre matriz em python ':=^150}")
print('\33[1;32m' + "~" * 150 + '\33[m')

print('\33[34mdigite um valor para: ')  

count = 0
count2 = 0
num_even = []
num_3c = []
matriz = []

for i in range(1, 10):
        
    num = int(input(f'\33[34m[{count}, {count2}] =>\33[33m '))
    matriz.append([num])
    
    if num % 2 == 0:
        num_even.append(num)
    
    count2 += 1
    if count >= 2:
        num_3c.append(num)
        
    if count2 == 3:
        count2 = 0
        count +=1
    


bigger = sum(matriz[3:6], [])
bigger.sort()
num_even.sort()

print('\33[1;32m' + "~" * 150 + '\33[0;33m')
for n in range(0, 9):
    print(matriz[n], end='')
    if n in [2,5,8]:
        print()
        
print(f'\33[34mA soma de todos os valores pares \33[33m{num_even} \33[34msão: \33[33m{sum(num_even)}')
print(f'\33[34mA soma dos valores da terceira coluna \33[33m{num_3c} => {sum(num_3c)}')
print(f'\33[34mO maior valor da segunda coluna \33[33m{sum(matriz[3:6], [])} \33[34mé \33[33m{bigger[-1]}')
print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(164, 'x'), '\33[0;m')