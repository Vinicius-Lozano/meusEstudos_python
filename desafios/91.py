from random import randint
from operator import itemgetter
from time import sleep

print("\33[1;32m" + "~" * 145)
print('\33[34m' + f"{' Dicionário em Python ':=^145}")
print('\33[1;32m' + "~" * 145 + '\33[m')

players = {'player': None, 'dice': None}
game = []

for i in range(1,5):
    players['player'] = i
    players['dice'] = randint(1,6)
    game.append(players.copy())

for p in game:
    print(f'\33[34mO jogador \33[33m{p['player']} \33[34mtirou \33[33m{p['dice']}')
    sleep(0.7)
    
game.sort(key=itemgetter('dice'), reverse=True)

print('\33[1;32m' + "~" * 145 + '\33[m')
print('\33[31mResultados')
print('\33[1;32m' + "~" * 145 + '\33[m')

a = 1
for p in game:
    print(f'\33[33m{a}° \33[34mlugar foi o jogador \33[33m{p['player']} \33[34mque tirou \33[33m{p['dice']} \33[34mno dado')
    a+=1

print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(159, 'x'), '\33[0;m')