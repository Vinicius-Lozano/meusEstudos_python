print("\33[1;32m" + "~" * 150)
print('\33[34m' + f"{' matriz em python ':=^150}")
print('\33[1;32m' + "~" * 150 + '\33[m')

print('\33[34mdigite um valor para: ')  

count = 0
count2 = 0
num_list = []
matriz = []

for i in range(1, 10):
        
    num = int(input(f'\33[34m[{count}, {count2}] =>\33[33m '))
    matriz.append([num])
    num_list.append(num)
    
    count2 += 1
    
    if count2 == 3:
        count2 = 0
        count +=1
        

print('\33[1;32m' + "~" * 150 + '\33[33m')
for n in range(0, 9):
    print(matriz[n], end='')
    if n in [2,5,8]:
        print()
print('\33[1;32m' + "~" * 150 + '\33[33m')
print('-' * 7)
print(f'|{'|'.join(str(num_list[n]) for n in range(0,3))}|')
print('-' * 7)
print(f'|{'|'.join(str(num_list[n]) for n in range(3,6))}|')
print('-' * 7)
print(f'|{'|'.join(str(num_list[n]) for n in range(6,9))}|')
print('-' * 7)
print('\33[33m' + '\33[1;31m FIM \33[1;33m'.center(164, 'x'), '\33[0;m')
        