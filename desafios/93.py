from time import sleep

print("\33[1;32m" + "~" * 145)
print('\33[34m' + f"{' Cadastro de Jogador de Futebol ':=^145}")
print('\33[1;32m' + "~" * 145 + '\33[m')

player = {}
gols = []

player['nome'] = str(input('\33[34mDigite o Nome do jogador:\33[33m '))
partidas = int(input('\33[34mQuantas partidas ele jogou?\33[33m '))

for p in range(1, partidas+1):
    gol = int(input(f'\33[34mGols na partida \33[33m{p} =>\33[31m '))
    gols.append(gol)
total_gols = sum(gols)
player['gols'] = gols
player['total'] = total_gols

print('\33[1;32m' + "~" * 145 + '\33[m')
info_array = [f'\33[34m{k}: \33[33m{v}' for k, v in player.items()]
print(f' \33[31m| '.join(info_array))

print('\33[1;32m' + "~" * 145 + '\33[m')
print(f'\33[34mO jogador \33[33m{player["nome"]} \33[34mjogou \33[33m{partidas} \33[34mpartidas!')
for i, g in enumerate(player['gols']):
    print(f'    \33[34m- partida \33[33m{i+1} \33[34m=> \33[33m{g} \33[34mgols')
    sleep(0.5)
print(f'\33[34m\nTotal \33[33m{player["total"]} \33[34mgols!')  

print('\33[1;33m' + '\33[1;31m FIM \33[1;33m'.center(159, 'x'), '\33[0;m')
