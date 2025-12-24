from random import sample
from time import sleep

print("\33[1;32m" + "~" * 150)
print('\33[34m' + f"{' Palpites para mega sena ':=^150}")
print('\33[1;32m' + "~" * 150 + '\33[m')


j = int(input('\33[34mQuantos jogos deseja gerar?\33[33m '))
for i in range(1, j+1):
    print(f'\33[34mJogo {i} => \33[33m{sample(range(1, 60), 6)}')
    sleep(0.4)

print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(164, 'x'), '\33[0;m')