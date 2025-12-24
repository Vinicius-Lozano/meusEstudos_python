from time import sleep

print("\33[1;32m" + "~" * 145)
print('\33[34m' + f"{' Aprimorando os Dicionários ':=^145}")
print('\33[1;32m' + "~" * 145 + '\33[m')

player = {
    'id': None,
    'nome': None,
    'partidas': None,
    'gols': None,
    'total': None
}
game = []
gols = []
id = 1

while True:
    player['id'] = id
    player['nome'] = str(input('\33[34mDigite o Nome do jogador:\33[33m '))
    player['partidas'] = int(input('\33[34mQuantas partidas ele jogou?\33[33m '))
    
    for p in range(1, player['partidas']+1):
        gols.append(int(input(f'\33[34mGols na partida \33[33m{p} =>\33[31m ')))
        
    total_gols = sum(gols)
    player['gols'] = gols[:]
    player['total'] = total_gols
    
    gols.clear()
    game.append(player.copy())
    id += 1
    stop = input('Parar? ')
    if stop == 's':
        break

print(game)

print('\33[33mJogadores cadastrados: ')
print(''.join(f'{k.upper():<25}' for k in player.keys()))

line = '-' * 105
print(line.center(2))
 
for p in game:
    for v in p.values():
        print(f'{str(v):<25}', end='')
    print()

while True:
    jgid = int(input('\33[34mEscolha um id ou 0 para Teminar:\33[33m '))
    
    if jgid == 0:
        break
    
    find = False
    for p in game:
        if p['id'] == jgid:
            
            print('\33[1;32m' + "~" * 145 + '\33[m')
            info_array = [f'\33[34m{k}: \33[33m{v}' for k, v in p.items()]
            print(' \33[31m| '.join(info_array))
            
            print('\33[1;32m' + "~" * 145 + '\33[m')
            print(f'\33[34mO jogador \33[33m{p["nome"]} \33[34mjogou \33[33m{p['partidas']} \33[34mpartidas!')
            for i, g in enumerate(p['gols']):
                print(f'    \33[34m- partida \33[33m{i+1} \33[34m=> \33[33m{g} \33[34mgols')
                sleep(0.5)
            print(f'\33[34m\nTotal \33[33m{player["total"]} \33[34mgols!')
            find = True
            break
        if not find:
            print('jogador não encontrado') 

print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(159, 'x'), '\33[0;m')
